# CQRS — Read Model Synchronization & Eventual Consistency

## Template 4: Read Model Synchronization

```python
class ReadModelSynchronizer:
    """Keeps read models in sync with events."""

    def __init__(self, event_store, read_db, projections: List[Projection]):
        self.event_store = event_store
        self.read_db = read_db
        self.projections = {p.name: p for p in projections}

    async def run(self):
        """Continuously sync read models."""
        while True:
            for name, projection in self.projections.items():
                await self._sync_projection(projection)
            await asyncio.sleep(0.1)

    async def _sync_projection(self, projection: Projection):
        checkpoint = await self._get_checkpoint(projection.name)

        events = await self.event_store.read_all(
            from_position=checkpoint,
            limit=100
        )

        for event in events:
            if event.event_type in projection.handles():
                try:
                    await projection.apply(event)
                except Exception as e:
                    # Log error, possibly retry or skip
                    logger.error(f"Projection error: {e}")
                    continue

            await self._save_checkpoint(projection.name, event.global_position)

    async def rebuild_projection(self, projection_name: str):
        """Rebuild a projection from scratch."""
        projection = self.projections[projection_name]

        # Clear existing data
        await projection.clear()

        # Reset checkpoint
        await self._save_checkpoint(projection_name, 0)

        # Rebuild
        while True:
            checkpoint = await self._get_checkpoint(projection_name)
            events = await self.event_store.read_all(checkpoint, 1000)

            if not events:
                break

            for event in events:
                if event.event_type in projection.handles():
                    await projection.apply(event)

            await self._save_checkpoint(
                projection_name,
                events[-1].global_position
            )
```

## Template 5: Eventual Consistency Handling

```python
class ConsistentQueryHandler:
    """Query handler that can wait for consistency."""

    def __init__(self, read_db, event_store):
        self.read_db = read_db
        self.event_store = event_store

    async def query_after_command(
        self,
        query: Query,
        expected_version: int,
        stream_id: str,
        timeout: float = 5.0
    ):
        """
        Execute query, ensuring read model is at expected version.
        Used for read-your-writes consistency.
        """
        start_time = time.time()

        while time.time() - start_time < timeout:
            # Check if read model is caught up
            projection_version = await self._get_projection_version(stream_id)

            if projection_version >= expected_version:
                return await self.execute_query(query)

            # Wait a bit and retry
            await asyncio.sleep(0.1)

        # Timeout - return stale data with warning
        return {
            "data": await self.execute_query(query),
            "_warning": "Data may be stale"
        }

    async def _get_projection_version(self, stream_id: str) -> int:
        """Get the last processed event version for a stream."""
        async with self.read_db.acquire() as conn:
            return await conn.fetchval(
                "SELECT last_event_version FROM projection_state WHERE stream_id = $1",
                stream_id
            ) or 0
```
