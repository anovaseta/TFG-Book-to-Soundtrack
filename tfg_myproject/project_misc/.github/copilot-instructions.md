# Copilot Instructions for AI Agents

## Project Overview
This project is a set of scripts for scraping book data using the StoryGraph API and processing the results. The main workflow involves reading book titles from `book_db.txt`, querying the StoryGraph API for metadata, and saving the results to JSON files. The codebase is Python-based and uses a local virtual environment in `testpip_tfg/`.

## Key Components
- `scrape_books_db.py`: Main script for scraping book data. Reads from `book_db.txt`, queries the API, and writes results to `db_output.json`. Handles errors and logs rejected books to `rejects.txt`.
- `db_final.py`: Processes the output JSON to deduplicate and summarize the scraped data.
- `script1.py`: Example script for initial API testing and experimentation.
- `book_db.txt`: List of book titles (one per line) to be processed.
- `testpip_tfg/`: Python virtual environment with dependencies (not source code).

## Developer Workflows
- **Run scraping:** Execute `scrape_books_db.py` to fetch book data. Use Ctrl+C to gracefully stop and save progress.
- **Process results:** Run `db_final.py` to deduplicate and count books in the final database.
- **API testing:** Use `script1.py` for quick API checks or debugging.

## Patterns & Conventions
- All file paths are relative to the project root.
- API interaction is encapsulated in the `Book` class from the external `storygraph_api` package.
- Error handling: Failed lookups are logged to `rejects.txt`.
- Output is always written as pretty-printed JSON.
- Use `signal_handler` in long-running scripts to ensure files are closed and data is saved on interruption.

## External Dependencies
- `storygraph_api` (installed in the virtual environment)
- Standard Python libraries: `json`, `signal`, `sys`

## Example Usage
```bash
# Activate the virtual environment
source testpip_tfg/bin/activate

# Run the main scraping script
python scrape_books_db.py

# Process the output
python db_final.py
```

## Notes
- The project does not use a build system or test framework.
- All scripts are intended to be run from the project root.
- Update `book_db.txt` to change the set of books to process.

---
For questions or improvements, update this file to help future AI agents and developers.
