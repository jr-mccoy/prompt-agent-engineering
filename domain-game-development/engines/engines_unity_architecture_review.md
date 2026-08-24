---
title: "Unity Project Architecture Review"
category: game-development/engines
description: "Review Unity project architecture covering MonoBehaviour lifecycle, ScriptableObject usage, assembly definitions, and render pipeline selection"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - QA-02
difficulty: intermediate
tags:
  - unity
  - architecture
  - code-review
  - monobehaviour
  - scriptableobject
  - assembly-definitions
updated: "2026-03-19"
---

# Unity Project Architecture Review

**Objective:** Review Unity project architecture for proper MonoBehaviour lifecycle usage, ScriptableObject data patterns, assembly definition organization, render pipeline selection (URP/HDRP/Built-in), package dependencies, and overall project structure.

**When to Use:**
- Reviewing a Unity project before entering production or shipping
- Auditing architecture decisions in a growing codebase
- Evaluating project structure for team scalability
- Assessing render pipeline fitness for target platform
- Reviewing MonoBehaviour usage patterns for performance concerns
- Checking dependency management and assembly definition organization
- Don't use when: reviewing individual script logic (use general C# code review instead)

**Instructions:**

1. **Review Project Structure**
   - Evaluate folder organization — standard conventions (Scripts/, Prefabs/, Materials/, Scenes/, etc.) vs feature-based organization
   - Check assembly definition (.asmdef) coverage — are scripts organized into logical assemblies or all in the default Assembly-CSharp?
   - Review Package Manager dependencies (manifest.json) — are packages version-pinned? Are deprecated packages present?
   - Check for proper .gitignore — Library/, Temp/, obj/ excluded; .meta files included
   - Verify Scenes folder organization and scene loading strategy (single scene, additive, addressable)
   - Check for Assets/Plugins vs Package Manager for third-party code

2. **Analyze MonoBehaviour Patterns**
   - **Lifecycle method usage:**
     - `Awake()` — initialization that does not depend on other objects (self-setup)
     - `OnEnable()` — subscribe to events, register with managers
     - `Start()` — initialization that depends on other objects being Awake'd
     - `OnDisable()` — unsubscribe from events, deregister
     - `OnDestroy()` — final cleanup, null-check before accessing other objects
   - **Update method selection:**
     - `Update()` — input handling, non-physics per-frame logic
     - `FixedUpdate()` — physics forces, Rigidbody manipulation
     - `LateUpdate()` — camera follow, post-physics adjustments
   - Check for script execution order dependencies — are they documented or relying on implicit ordering?
   - Flag MonoBehaviours with both Awake() and Start() doing similar work
   - Verify coroutine lifecycle — are coroutines stopped in OnDisable/OnDestroy?

3. **Evaluate Data Architecture**
   - **ScriptableObjects vs MonoBehaviours for data:**
     - ScriptableObjects for shared configuration data (weapon stats, enemy definitions, level configs)
     - MonoBehaviours for instance-specific runtime state
   - Check `[SerializeField]` vs `public` — prefer SerializeField for Inspector-exposed private fields
   - Review custom Editor/Inspector scripts — are they in Editor assembly definitions?
   - Check for proper use of `[CreateAssetMenu]` for ScriptableObject creation
   - Verify data-driven patterns — are magic numbers in code or externalized to data assets?
   - Check for ScriptableObject event channels (event-driven architecture pattern)

4. **Check Render Pipeline Fit**
   - **URP (Universal Render Pipeline)** — appropriate for mobile, VR, 2D, performance-sensitive 3D
   - **HDRP (High Definition Render Pipeline)** — appropriate for high-fidelity PC/console, realistic lighting
   - **Built-in (Legacy)** — check if migration to SRP is warranted or if project is too far along
   - Verify shader compatibility — are custom shaders written for the correct pipeline (Shader Graph vs hand-written)?
   - Check post-processing setup (Volume-based for SRP, legacy PostProcessingStack v2 for Built-in)
   - Evaluate if the project uses pipeline-specific features that lock in the choice

5. **Review Dependency Management**
   - Check `Packages/manifest.json` for version pinning (avoid `"latest"` or floating versions)
   - Identify deprecated packages (e.g., legacy Input Manager when New Input System is available)
   - Review Asset Store dependencies — are they updatable or forked?
   - Check for duplicate functionality (e.g., DOTween + LeanTween, multiple JSON libraries)
   - Verify test framework setup (com.unity.test-framework in manifest)
   - Check for com.unity.addressables if project has significant asset loading needs

6. **CRITICAL: Verification Checklist**
   - [ ] **No FindObjectOfType in hot paths** — FindObjectOfType, FindObjectsOfType, and FindWithTag are O(n) scene scans; never in Update/FixedUpdate
   - [ ] **No Instantiate/Destroy without pooling in frequent operations** — bullets, particles, and other frequently spawned objects use object pooling
   - [ ] **No missing null checks after GetComponent** — GetComponent can return null if component is not present; always check before use
   - [ ] **No string-based method invocations** — SendMessage, BroadcastMessage, and Invoke with string parameters are error-prone and slow; use direct references or UnityEvents
   - [ ] **No Camera.main in Update** — Camera.main does a FindWithTag internally; cache the reference
   - [ ] **No empty MonoBehaviour callbacks** — empty Update(), Start(), or FixedUpdate() methods still have overhead from native-to-managed calls
   - [ ] **Assembly definitions present** — at minimum, separate Runtime, Editor, and Tests assemblies

**False-Positive Prevention:**

| Mistake | Correction |
|---------|------------|
| ❌ Flagging Update() as inherently bad or always a performance problem | ✅ Update() is the correct pattern for per-frame logic like input reading and state machines; flag only when the work inside could be event-driven or timer-based |
| ❌ Requiring DOTS/ECS for simple games | ✅ MonoBehaviour + GameObjects is perfectly appropriate for games with fewer than ~1000 active entities; DOTS adds complexity that small projects do not need |
| ❌ Demanding ScriptableObjects for all data | ✅ Simple config values in MonoBehaviours via SerializeField are fine for small projects; ScriptableObjects shine when data is shared across prefabs or needs designer editing |
| ❌ Flagging Singleton pattern as always wrong | ✅ Singletons for truly global systems (AudioManager, SaveManager) are acceptable in small-to-medium projects; flag only when there are 10+ singletons indicating missing architecture |
| ❌ Ignoring target platform when reviewing pipeline choice | ✅ URP is correct for mobile even if it limits visual fidelity; HDRP is correct for PC/console showcase titles; evaluate fitness for target, not absolute quality |
| ❌ Requiring assembly definitions for tiny prototypes | ✅ Assembly definitions add compile-time benefits but overhead for projects with <20 scripts; recommend them for production, not prototypes |

**Expected Output:** A structured architecture review that includes:

1. Project structure assessment with folder organization evaluation
2. MonoBehaviour lifecycle usage audit
3. Data architecture review (ScriptableObject patterns, serialization)
4. Render pipeline fitness evaluation
5. Dependency management assessment
6. Verification checklist results with specific findings

**Example Output:**

```markdown
# Unity Architecture Review — Mobile Puzzle Game

**Project:** GemCrush (Unity 2023.2 LTS)
**Target Platforms:** iOS, Android
**Render Pipeline:** URP 14.0.9
**Scripts Reviewed:** 47 C# files
**Review Date:** 2026-03-19

---

## 1. Project Structure Assessment

### Folder Organization

```
Assets/
├── _Project/                  ✅ Good: project-specific prefix
│   ├── Scripts/
│   │   ├── Core/              Game managers, state machine
│   │   ├── Gameplay/          Board logic, gem matching
│   │   ├── UI/                Menus, HUD, popups
│   │   ├── Audio/             Audio manager, sound banks
│   │   └── Data/              ScriptableObject definitions
│   ├── Prefabs/
│   │   ├── Gems/              Individual gem prefabs
│   │   ├── Effects/           VFX prefabs
│   │   └── UI/                UI prefabs
│   ├── ScriptableObjects/     ✅ Separate from Scripts
│   │   ├── LevelDefinitions/
│   │   ├── GemTypes/
│   │   └── AudioEvents/
│   ├── Materials/
│   ├── Textures/
│   ├── Animations/
│   ├── Scenes/
│   │   ├── Boot.unity
│   │   ├── MainMenu.unity
│   │   └── Gameplay.unity
│   └── Editor/                Editor-only scripts
├── Plugins/                   Third-party native plugins
└── StreamingAssets/           Platform-specific data
```

**Findings:**
- ✅ Clear separation between project assets and third-party content
- ✅ ScriptableObjects in dedicated folder, not mixed with scripts
- ⚠️ No `Tests/` folder found — unit and play-mode tests are missing
- ⚠️ `Editor/` folder is inside `_Project/Scripts/` — should have its own
  assembly definition to prevent editor code shipping in builds

### Assembly Definition Coverage

| Assembly | Path | References | Status |
|----------|------|------------|--------|
| GemCrush.Runtime | _Project/Scripts/ | Unity defaults | ✅ Present |
| GemCrush.Editor | _Project/Editor/ | GemCrush.Runtime | ❌ **Missing** |
| GemCrush.Tests | Tests/ | — | ❌ **Missing (no tests)** |

**Issue:** Without an Editor assembly definition, editor-only code (custom
inspectors, editor windows) will be included in player builds, increasing
build size and potentially causing build errors on IL2CPP.

**Fix:** Create `_Project/Editor/GemCrush.Editor.asmdef`:
```json
{
    "name": "GemCrush.Editor",
    "rootNamespace": "GemCrush.Editor",
    "references": ["GemCrush.Runtime"],
    "includePlatforms": ["Editor"],
    "excludePlatforms": [],
    "allowUnsafeCode": false
}
```

---

## 2. MonoBehaviour Lifecycle Audit

### Lifecycle Ordering Issue

File: `BoardManager.cs`
```csharp
// PROBLEM: Start() depends on GemFactory being initialized,
// but execution order is not guaranteed
public class BoardManager : MonoBehaviour
{
    private GemFactory _gemFactory;

    void Start()
    {
        // GemFactory.Instance may be null if GemFactory.Awake()
        // hasn't run yet
        _gemFactory = GemFactory.Instance;
        GenerateBoard();
    }
}

public class GemFactory : MonoBehaviour
{
    public static GemFactory Instance { get; private set; }

    void Awake()
    {
        Instance = this;
        LoadGemPrefabs();
    }
}
```

**Fix Options:**
1. Set Script Execution Order: GemFactory before BoardManager
2. Better: Use dependency injection instead of singleton timing:
```csharp
public class BoardManager : MonoBehaviour
{
    [SerializeField] private GemFactory _gemFactory; // Inspector reference

    void Start()
    {
        // No timing dependency — reference is set in editor
        GenerateBoard();
    }
}
```

### Update Method Misuse

File: `ScoreDisplay.cs`
```csharp
// BEFORE: Polls score value every frame
public class ScoreDisplay : MonoBehaviour
{
    [SerializeField] private TextMeshProUGUI _scoreText;

    void Update()
    {
        // Runs every frame even when score hasn't changed
        _scoreText.text = $"Score: {GameManager.Instance.CurrentScore}";
    }
}

// AFTER: Event-driven update
public class ScoreDisplay : MonoBehaviour
{
    [SerializeField] private TextMeshProUGUI _scoreText;

    void OnEnable()
    {
        GameManager.OnScoreChanged += UpdateScoreDisplay;
    }

    void OnDisable()
    {
        GameManager.OnScoreChanged -= UpdateScoreDisplay;
    }

    private void UpdateScoreDisplay(int newScore)
    {
        _scoreText.text = $"Score: {newScore}";
    }
}
```
**Impact:** Eliminates per-frame string allocation and text rebuild
when score is static (which is 95%+ of frames).

### Empty Callback Found

File: `GemVisual.cs`, Line 12
```csharp
// PROBLEM: Empty Update has measurable overhead due to
// native-to-managed callback cost (~0.02ms per 1000 instances)
void Update()
{
    // TODO: Add sparkle animation
}
```
**Fix:** Remove the empty method. Add it back when the feature is implemented.
With 64 gems on screen, this wastes ~1.3ms per frame on mobile.

### Coroutine Lifecycle Issue

File: `TutorialManager.cs`
```csharp
// PROBLEM: Coroutine not stopped on disable — will throw
// MissingReferenceException if object is destroyed mid-sequence
public class TutorialManager : MonoBehaviour
{
    void Start()
    {
        StartCoroutine(ShowTutorialSequence());
    }

    IEnumerator ShowTutorialSequence()
    {
        yield return new WaitForSeconds(2f);
        _highlightArrow.SetActive(true);  // may crash if destroyed
        yield return new WaitForSeconds(3f);
        _dialogBox.Show("Tap a gem!");     // may crash if destroyed
    }
}

// FIX: Track and stop coroutine
private Coroutine _tutorialCoroutine;

void Start()
{
    _tutorialCoroutine = StartCoroutine(ShowTutorialSequence());
}

void OnDisable()
{
    if (_tutorialCoroutine != null)
    {
        StopCoroutine(_tutorialCoroutine);
        _tutorialCoroutine = null;
    }
}
```

---

## 3. Data Architecture Review

### ScriptableObject Usage — Well Done

```csharp
[CreateAssetMenu(fileName = "New Gem Type", menuName = "GemCrush/Gem Type")]
public class GemTypeDefinition : ScriptableObject
{
    [Header("Identity")]
    public string GemName;
    public GemColor Color;

    [Header("Visuals")]
    public Sprite GemSprite;
    public Sprite GemGlowSprite;
    public Color ParticleColor;

    [Header("Gameplay")]
    public int BaseScoreValue = 10;
    public bool IsSpecial;

    [Header("Audio")]
    public AudioClip MatchSound;
    public AudioClip SelectSound;
}
```
✅ Good: Shared data externalized to assets. Designers can create new gem
types without touching code. CreateAssetMenu provides easy authoring.

### SerializeField vs Public Issue

File: `BoardManager.cs`
```csharp
// BEFORE: Public fields exposed unintentionally
public class BoardManager : MonoBehaviour
{
    public int BoardWidth = 8;       // Exposed AND accessible from any script
    public int BoardHeight = 8;
    public float GemSize = 1.0f;
    public GameObject GemPrefab;     // Anyone can reassign at runtime
    public Transform BoardParent;
}

// AFTER: Private with SerializeField
public class BoardManager : MonoBehaviour
{
    [SerializeField] private int _boardWidth = 8;
    [SerializeField] private int _boardHeight = 8;
    [SerializeField] private float _gemSize = 1.0f;
    [SerializeField] private GameObject _gemPrefab;
    [SerializeField] private Transform _boardParent;

    public int BoardWidth => _boardWidth;   // Read-only public access
    public int BoardHeight => _boardHeight;
}
```

### Missing Data-Driven Pattern

File: `LevelManager.cs`, Line 34
```csharp
// PROBLEM: Level parameters hardcoded
private void SetupLevel(int levelNumber)
{
    switch (levelNumber)
    {
        case 1: _moveLimit = 20; _targetScore = 500; break;
        case 2: _moveLimit = 18; _targetScore = 800; break;
        case 3: _moveLimit = 15; _targetScore = 1200; break;
        // ... 47 more cases
    }
}
```
**Fix:** Create a `LevelDefinition` ScriptableObject:
```csharp
[CreateAssetMenu(menuName = "GemCrush/Level Definition")]
public class LevelDefinition : ScriptableObject
{
    public int LevelNumber;
    public int MoveLimit;
    public int TargetScore;
    public int BoardWidth = 8;
    public int BoardHeight = 8;
    public GemTypeDefinition[] AvailableGems;
}
```

---

## 4. Render Pipeline Assessment

**Current Pipeline:** URP 14.0.9
**Target Platforms:** iOS (iPhone 8+), Android (Vulkan/OpenGLES 3.1)

**Verdict: ✅ Correct choice for mobile puzzle game.**

| Factor | Assessment |
|--------|------------|
| Performance budget | URP's SRP Batcher and batching work well for 2D sprite-heavy game |
| Visual requirements | 2D puzzle game does not need HDRP's PBR/ray tracing |
| Shader compatibility | All shaders use Shader Graph (URP) — no legacy shader issues |
| Post-processing | URP Volume-based bloom and color grading — appropriate for gem sparkle effects |
| Build size | URP adds ~15MB less than HDRP to final build |

**Recommendations:**
- Enable SRP Batcher in URP Asset (currently disabled)
- Set `Opaque Downsampling` to `None` for 2D — not needed
- Disable depth texture and opaque texture generation (not used in 2D)

---

## 5. Dependency Management

### Package Manifest Review

```json
{
    "dependencies": {
        "com.unity.2d.sprite": "1.0.0",
        "com.unity.2d.tilemap": "1.0.0",
        "com.unity.textmeshpro": "3.0.6",
        "com.unity.ugui": "1.0.0",
        "com.unity.render-pipelines.universal": "14.0.9",
        "com.unity.inputsystem": "1.7.0",
        "com.unity.addressables": "1.21.19",
        "com.unity.analytics": "3.7.1",
        "com.demigiant.dotween": "1.2.765"
    }
}
```

| Package | Status | Note |
|---------|--------|------|
| com.unity.inputsystem | ✅ | New Input System — correct choice |
| com.unity.addressables | ⚠️ | Installed but only 3 assets use it — overhead may not be justified for a small puzzle game |
| com.unity.analytics | ⚠️ | Legacy analytics — consider Unity Gaming Services or custom |
| com.unity.2d.tilemap | ⚠️ | Imported but unused — no tilemaps in project; remove |
| com.unity.test-framework | ❌ | **Missing** — no test framework installed |
| DOTween | ✅ | Version-pinned, actively used for gem animations |

---

## 6. Verification Checklist Results

- [ ] **No FindObjectOfType in hot paths** — **FAIL**: `GemMatcher.cs:23`
      calls `FindObjectOfType<BoardManager>()` inside the match-checking
      loop, which runs on every player move
- [ ] **No Instantiate/Destroy without pooling** — **FAIL**: Gems are
      Instantiate'd on board generation and Destroy'd on matches. With
      64+ gems created per level and frequent matches, this causes GC
      spikes on mobile. Implement ObjectPool<Gem>.
- [x] **No missing null checks after GetComponent** — PASS: all
      GetComponent calls check for null
- [x] **No string-based method invocations** — PASS: no SendMessage
      or BroadcastMessage found
- [ ] **No Camera.main in Update** — **FAIL**: `InputHandler.cs:45`
      calls `Camera.main` every frame for screen-to-world raycasting
- [ ] **No empty MonoBehaviour callbacks** — **FAIL**: `GemVisual.cs`
      has empty Update() (see Section 2)
- [ ] **Assembly definitions present** — **PARTIAL**: Runtime asmdef
      present but Editor and Tests asmdefs missing

---

## Summary

| Category | Status | Findings |
|----------|--------|----------|
| Project Structure | ⚠️ | Missing Editor asmdef, no test infrastructure |
| MonoBehaviour Lifecycle | 🔴 | Execution order dependencies, uncancelled coroutines |
| Data Architecture | ✅ | Good ScriptableObject usage, some hardcoded levels remain |
| Render Pipeline | ✅ | URP is correct choice, minor optimization settings needed |
| Dependencies | ⚠️ | Unused packages, missing test framework |
| Verification | 🔴 | 4 of 7 checks failed |

**Top 3 Actions:**
1. Implement object pooling for gems — biggest mobile performance win
2. Cache Camera.main and FindObjectOfType results — eliminate per-frame allocations
3. Create Editor assembly definition — prevent editor code in builds
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) — opens with precise scope covering lifecycle, data, pipeline, and structure
- ST-02 (Structured Sequential Instructions) — six numbered steps from project structure through verification
- RT-02 (Systematic Classification) — classifies findings by category and severity across multiple dimensions
- RT-05 (Evidence-Based Reasoning) — every finding includes specific file references and before/after code
- QA-02 (False-Positive Prevention) — explicit table preventing over-flagging of Update(), Singletons, and DOTS recommendations

**Related Prompts:**
- `domain-game-development/performance/performance_profiling_analysis.md` — Frame-level profiling for Unity projects
- `domain-game-development/engines/engines_godot_architecture_review.md` — Architecture review for Godot projects
- `domain-software-engineering/analysis/architecture/architecture_layer_identification.md` — General architectural layer analysis
- `domain-software-engineering/analysis/quality/quality_code_complexity_analysis.md` — Code complexity metrics
