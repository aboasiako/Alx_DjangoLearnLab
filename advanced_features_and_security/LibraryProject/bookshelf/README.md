# Permissions and Groups Setup

## Overview
This setup defines custom permissions for controlling access to specific actions on `MyModel` instances. Groups such as Editors, Viewers, and Admins are created and assigned appropriate permissions.

## Custom Permissions
- `can_view`: Allows viewing of instances.
- `can_create`: Allows creating new instances.
- `can_edit`: Allows editing instances.
- `can_delete`: Allows deleting instances.

## Groups Configuration
- **Editors**: Permissions - can_create, can_edit.
- **Viewers**: Permissions - can_view.
- **Admins**: All permissions.

## Enforcing Permissions in Views
Views use `@permission_required` to restrict access based on user permissions.
