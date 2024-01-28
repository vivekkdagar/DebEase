# DebEase

DebEase is a full-stack Django web application designed to simplify system configuration tasks on Debian-based systems. The application provides a user-friendly interface for performing various tasks such as installing packages, configuring login managers, installing drivers, and more.

## Features

- **Change Default Login Manager:** Allows users to change the default login manager on their Debian system.

- **Install Microcode:** Installs CPU microcode for improved performance and compatibility.

- **Install GPU Drivers:** Installs GPU drivers for better graphics performance.

- **Replace apt with Nala:** Replaces the default package manager (apt) with Nala.

- **Install Battery Saver:** Installs and configures TLP for improved battery life.

- **Install App Launcher:** Installs ULauncher as an application launcher.

- **Configure Firewall:** Sets up the Uncomplicated Firewall (UFW) for enhanced security.

- **Install Timeshift:** Installs Timeshift, a backup tool for creating system snapshots.

- **Install WebApp Manager:** Installs Linux Mint's web app manager.

- **Setup Custom Scripts:** Configures custom scripts to streamline accessibility.

- **Configure Terminal Aliases:** Sets up aliases for commonly used terminal commands.

- **Install KDE-Connect:** Installs KDE-Connect for seamless device integration.

- **Enhance Terminal:** Installs and configures Starship for a customized terminal prompt.

- **Make LibreOffice Look Better:** Applies a custom theme to LibreOffice for improved aesthetics.

## Prerequisites

- Debian-based system (tested on Debian)
- Python 3
- Django
- Puppet
- Additional dependencies as specified in `dependencies.sh`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/DebEase.git
   cd DebEase
   ```

2. Run the dependencies script:

   ```bash
   sudo bash resources/dependencies.sh
   ```

3. Apply migrations and start the Django development server:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

4. Access the application in your web browser at [http://localhost:8000](http://localhost:8000).

## Usage

1. Visit the homepage and select the tasks you want to perform.
2. Click the "Run" button to execute the selected tasks.

## Contributing

Contributions are welcome! Please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Special thanks to [contributors](CONTRIBUTORS.md) who have contributed to this project.
