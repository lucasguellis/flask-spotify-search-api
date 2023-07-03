# Flask Project - Spotify Album Information Generator

This Flask project is a web application and API that retrieves information about albums from the Spotify API. The application allows users to search for an album and view its details, such as the album cover image, the number of songs, the artist, and the release year. The project also aims to provide a functionality to generate custom images containing the album information, but this feature will be developed on a close future.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/lucasguellis/flask-spotify-search-api.git
   ```

2. Navigate to the project directory:

   ```
   cd flask-spotify-search-api
   ```

3. Create a virtual environment:

   ```
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - For Windows:

     ```
     venv\Scripts\activate
     ```

   - For Unix or Linux:

     ```
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Set up the required environment variables:

   - Create a `.env` file in the root directory of the project.
   - Add the following variables to the `.env` file:
     ```
     CLIENT_ID=your-spotify-client-id
     CLIENT_SECRET=your-spotify-client-secret
     TOKEN=fisrt-token-generated
     ```

2. Run the Flask development server:

   ```
   flask run
   ```
    
   ```
   python -m app
   ```

3. Open your web browser and visit `http://localhost:5000` to access the application.

## Features

- Album Search: Users can search for albums and retrieve information, including the album cover image, the number of songs, the artist, and the release year using route /search.
- Image Generation: Planned functionality to generate custom images containing the album information. (Work in progress)

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b my-new-feature`.
3. Make your changes and commit them: `git commit -am 'Add some feature'`.
4. Push the branch to your forked repository: `git push origin my-new-feature`.
5. Submit a pull request detailing your changes.