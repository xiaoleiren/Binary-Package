# Mandatory Sandbox Safety Checklist

Before any executable lab session:

## Tool Implementation
- [ ] Mock tools only: no real email, calendar, repository, payment, or student-record APIs
- [ ] All tool calls return predefined synthetic responses
- [ ] Tool implementations reviewed by instructor to confirm no hidden live side effects

## Network and Environment
- [ ] Network egress disabled (or restricted to local mock services only)
- [ ] Read-only file systems where possible; write operations target disposable state only
- [ ] Read-only templates available for reference (e.g., `env.tpl` files)

## Data and Credentials
- [ ] Synthetic records only; no real student or user data
- [ ] Fake credentials clearly marked as fake (e.g., `FAKE_API_KEY=changeme`)
- [ ] No real API keys, tokens, or secrets in configuration files

## Process and Resource Limits
- [ ] Student code runs in container or VM isolation
- [ ] CPU, memory, and time limits enforced
- [ ] Disposable state reset between runs
- [ ] Logs stored locally and treated as course artifacts

## Student Access
- [ ] Students informed that this is a controlled educational environment
- [ ] Students explicitly instructed not to test payloads on live systems
- [ ] Non-executable frozen-trace alternative available as equal option

## Verification
- [ ] Instructor runs a test case through the sandbox before student release
- [ ] All above checks verified and documented