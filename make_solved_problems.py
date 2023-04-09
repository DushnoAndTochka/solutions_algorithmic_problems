#!/usr/bin/env python3
import csv
import pathlib
import re

REGEX = re.compile('^<a href="(https://leetcode.com/problems/.+/)">.+')
CSV_HEADERS = ["problem_name", "problem_origin_url", "is_solved_problem"]


def get_solved_tasks(parent: pathlib.Path) -> set[tuple[str, str]]:
    solutions = parent / "solutions"
    solved = set()
    for solution in solutions.iterdir():
        problem_name = str(solution).split('/')[1]
        problem_readme = solution / "README.md"
        with open(problem_readme) as f:
            line = f.readlines()[-1]
            m = REGEX.match(line)
            assert m, problem_readme
            problem = m.group(1)
            assert problem not in solved, problem

        solution_path = solution / 'solution'
        if (solution_path in solution.iterdir()
                and solution_path / 'README.md' in solution_path.iterdir()):
            solved.add((problem_name, problem, True))
        else:
            solved.add((problem_name, problem, False))
    return sorted(solved)


def write_result(parent: pathlib.Path, solved: set[tuple[str, str]]) -> None:
    with open(parent / "solved_problems.csv", "wt") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(CSV_HEADERS)
        writer.writerows(solved)


def main():
    parent = pathlib.Path().parent
    solved_problems = get_solved_tasks(parent)
    write_result(parent, solved_problems)


if __name__ == "__main__":
    main()
