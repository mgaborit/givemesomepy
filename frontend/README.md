# Frontend

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 18.2.11.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The application will automatically reload if you change any of the source files.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory.

## Debugging with Firefox

### Configure
1. Add a new profile to Firefox
2. With new profile, in dev tools settings :
    * Enable browser chrome and add-on debugging toolboxes
    * Enable remote debugging
3. Install **Debugger for Firefox** VSCode extension
4. Add config to _launch.json_ :
```json
{
    "type": "firefox",
    "request": "attach",
    "name": "Attach",
    "url": "http://localhost:4200/",
    "webRoot": "${workspaceFolder}"
}
```

### Launch

1. Launch the dev server
```bash
ng serve
```

2. Launch Firefox in debug mode with specific profile
```bash
firefox -start-debugger-server -P <my_debug_profile>
```

3. Launch the debugger by pressing F5