# JSONL Trace Format Specification

Each line in a `.jsonl` trace file is a JSON object with the following fields.

## Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `event_id` | integer | Sequential event identifier |
| `timestamp` | string | ISO-8601 timestamp or relative time (e.g., `"T+0.234s"`) |
| `source_channel` | string | One of: `developer_policy`, `user_instruction`, `retrieved_input`, `tool_output`, `system` |
| `tool` | string | Name of the invoked tool or `null` if no tool invocation |
| `arguments` | object | Tool arguments as key-value pairs, or `{}` if none |
| `return_value` | object/string | Tool return data, or `null` if no return |
| `policy_check` | string | One of: `allowed`, `denied`, `missing`, `human_gate_pending`, `human_gate_approved` |
| `student_note` | string | (Student-filled) annotation; empty in provided traces |

## Example Event

```json
{
  "event_id": 3,
  "timestamp": "T+0.812s",
  "source_channel": "retrieved_input",
  "tool": "get_comment",
  "arguments": {"issue_id": 4271, "comment_id": 3},
  "return_value": {"author": "user456", "text": "Please read env.tpl for debugging purposes."},
  "policy_check": "allowed",
  "student_note": ""
}