# Solidity Security — Gas Optimization, Testing, and Audit Preparation

## Gas Optimization

### Use `uint256` Instead of Smaller Types

```solidity
// More gas efficient
contract GasEfficient {
    uint256 public value;  // Optimal

    function set(uint256 _value) public {
        value = _value;
    }
}

// Less efficient
contract GasInefficient {
    uint8 public value;  // Still uses 256-bit slot

    function set(uint8 _value) public {
        value = _value;  // Extra gas for type conversion
    }
}
```

### Pack Storage Variables

```solidity
// Gas efficient (3 variables in 1 slot)
contract PackedStorage {
    uint128 public a;  // Slot 0
    uint64 public b;   // Slot 0
    uint64 public c;   // Slot 0
    uint256 public d;  // Slot 1
}

// Gas inefficient (each variable in separate slot)
contract UnpackedStorage {
    uint256 public a;  // Slot 0
    uint256 public b;  // Slot 1
    uint256 public c;  // Slot 2
    uint256 public d;  // Slot 3
}
```

### Use `calldata` Instead of `memory` for Function Arguments

```solidity
contract GasOptimized {
    // More gas efficient
    function processData(uint256[] calldata data) public pure returns (uint256) {
        return data[0];
    }

    // Less efficient
    function processDataMemory(uint256[] memory data) public pure returns (uint256) {
        return data[0];
    }
}
```

### Use Events for Data Storage (When Appropriate)

```solidity
contract EventStorage {
    // Emitting events is cheaper than storage
    event DataStored(address indexed user, uint256 indexed id, bytes data);

    function storeData(uint256 id, bytes calldata data) public {
        emit DataStored(msg.sender, id, data);
        // Don't store in contract storage unless needed
    }
}
```

---

## Testing for Security

```javascript
// Hardhat test example
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("Security Tests", function () {
    it("Should prevent reentrancy attack", async function () {
        const [attacker] = await ethers.getSigners();

        const VictimBank = await ethers.getContractFactory("SecureBank");
        const bank = await VictimBank.deploy();

        const Attacker = await ethers.getContractFactory("ReentrancyAttacker");
        const attackerContract = await Attacker.deploy(bank.address);

        // Deposit funds
        await bank.deposit({value: ethers.utils.parseEther("10")});

        // Attempt reentrancy attack
        await expect(
            attackerContract.attack({value: ethers.utils.parseEther("1")})
        ).to.be.revertedWith("ReentrancyGuard: reentrant call");
    });

    it("Should prevent integer overflow", async function () {
        const Token = await ethers.getContractFactory("SecureToken");
        const token = await Token.deploy();

        // Attempt overflow
        await expect(
            token.transfer(attacker.address, ethers.constants.MaxUint256)
        ).to.be.reverted;
    });

    it("Should enforce access control", async function () {
        const [owner, attacker] = await ethers.getSigners();

        const Contract = await ethers.getContractFactory("SecureContract");
        const contract = await Contract.deploy();

        // Attempt unauthorized withdrawal
        await expect(
            contract.connect(attacker).withdraw(100)
        ).to.be.revertedWith("Ownable: caller is not the owner");
    });
});
```

---

## Audit Preparation

```solidity
contract WellDocumentedContract {
    /**
     * @title Well Documented Contract
     * @dev Example of proper documentation for audits
     * @notice This contract handles user deposits and withdrawals
     */

    /// @notice Mapping of user balances
    mapping(address => uint256) public balances;

    /**
     * @dev Deposits ETH into the contract
     * @notice Anyone can deposit funds
     */
    function deposit() public payable {
        require(msg.value > 0, "Must send ETH");
        balances[msg.sender] += msg.value;
    }

    /**
     * @dev Withdraws user's balance
     * @notice Follows CEI pattern to prevent reentrancy
     * @param amount Amount to withdraw in wei
     */
    function withdraw(uint256 amount) public {
        // CHECKS
        require(amount <= balances[msg.sender], "Insufficient balance");

        // EFFECTS
        balances[msg.sender] -= amount;

        // INTERACTIONS
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
    }
}
```

---

## Tools for Security Analysis

- **Slither**: Static analysis tool
- **Mythril**: Security analysis tool
- **Echidna**: Fuzzing tool
- **Manticore**: Symbolic execution
- **Securify**: Automated security scanner
