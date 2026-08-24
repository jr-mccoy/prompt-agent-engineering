# Remix / React Router Prompts

**Category:** Frontend Development / Remix
**Prompts:** 1

---

## Overview

Production-grade prompts for Remix (and React Router in framework mode), focused on its web-fundamentals-first data model: data lives on routes via loaders, mutations go through route actions, forms use progressive enhancement, and the UI stays in sync through revalidation. The coverage spans nested-route parallel loading, no-JS form behavior, error/catch boundaries, and mutation + revalidation. Prompts describe conventions and flag version-specific hook/API names for verification, since Remix and React Router are converging and evolving.

## Prompts

| Prompt | Description | Difficulty |
|--------|-------------|------------|
| [frontend_remix_data_loading.md](frontend_remix_data_loading.md) | Audit loaders/actions, nested-route parallel loading, progressive enhancement, error/catch boundaries, and mutation + revalidation; catch client fetches and state that should live on routes | Intermediate |

## Usage Examples

### Auditing Data Flow and Mutations
Use `frontend_remix_data_loading.md` to find:
- Client `useEffect` fetches where a route loader belongs (and the resulting waterfall)
- Forms built on raw `fetch` that break without JS and never revalidate
- Mutations that don't refresh affected loaders, leaving stale UI
- Routes with loaders/actions but no error boundary, blanking the app on failure
- Client state stores duplicating loader data and drifting from the server

## Key Concepts

- **Data on routes:** loaders fetch on the server; components read via the typed data hook. Nested loaders run in parallel, avoiding parent→child waterfalls.
- **Actions + revalidation:** writes go through route actions invoked by `<Form>`/`useSubmit`/`useFetcher`; completing an action revalidates affected loaders so the UI reflects server state.
- **Progressive enhancement:** framework `<Form>` submits and works without JavaScript, then enhances when JS loads — pending/optimistic UI builds on top.
- **Error/catch boundaries:** scope failures to the failing route segment instead of crashing the whole app; handle expected error responses distinctly from unexpected errors.
- **Server vs client state:** keep server data in loaders (revalidated), and reserve client state for genuinely client-only UI.

---

## Related Prompts

- [../nextjs/frontend_nextjs_app_router.md](../nextjs/frontend_nextjs_app_router.md) - Compare with Next.js App Router data conventions
- [../nextjs/frontend_nextjs_data_fetching.md](../nextjs/frontend_nextjs_data_fetching.md) - Server vs client data-fetching strategies
- [../react/frontend_react_server_components_streaming.md](../react/frontend_react_server_components_streaming.md) - Server-first rendering and streaming comparison
- [../architecture/frontend_state_management_selection.md](../architecture/frontend_state_management_selection.md) - Deciding server state vs client state
