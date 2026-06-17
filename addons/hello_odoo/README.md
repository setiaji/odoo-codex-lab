# Hello Odoo

Hello Odoo is the first training addon for the Odoo development lab.

## Features

- Adds a `Greeting` model for simple greeting messages.
- Provides tree, form, and search views.
- Adds a **Hello Odoo > Greetings** menu entry.
- Includes standard internal user access rights.
- Provides demo data for training environments.

## Model

Technical model: `hello.odoo.greeting`

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `title` | Char | Yes | - | Greeting title. |
| `message` | Text | No | - | Greeting message body. |
| `active` | Boolean | No | `True` | Enables archiving greetings. |

## Installation

1. Add this repository's `addons` directory to the Odoo addons path.
2. Update the Apps list.
3. Install **Hello Odoo**.

## License

LGPL-3
