import argparse
from .pubScraper import get_papers, save_to_csv  # 👈 Add the dot `.`
from .pubScraper import get_papers, save_to_csv


def main(str=None):
    parser = argparse.ArgumentParser(description="Fetch PubMed papers")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-f", "--file", type=str, help="Save results to CSV file")

    args = parser.parse_args()
    results = get_papers(args.query)

    if args.file:
        save_to_csv(results, args.file)
        print(f"Results saved to {args.file}")
    else:
        for paper in results:
            print(paper)


if __name__ == "__main__":
    main()
