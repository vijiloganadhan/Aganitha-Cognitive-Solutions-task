#📚 PubMed Fetcher

##📝 Description

A simple Python CLI tool to fetch PubMed research papers and save them as a CSV file.

#⚙️ Installation

**Clone the repository:**

git clone https://github.com/yourusername/pubmed-fetcher.git
cd pubmed-fetcher

**Install dependencies:**

poetry install

## Usage

Fetch and save papers to CSV:

poetry run get-papers-list "cancer treatment" -f results.csv

Fetch papers and display without saving:

poetry run get-papers-list "machine learning in medicine"

#🔑 API Key

Replace API_KEY in fetcher.py with your NCBI API key for better request limits.

#🛠 Troubleshooting

Ensure no program (like Excel) is using results.csv

Run the command with admin privileges if needed

Try saving to another location, e.g., C:/Users/Public/results.csv

#📜 License

MIT License. Feel free to use and modify! 🎉

