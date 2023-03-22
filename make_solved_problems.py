import pathlib
import re
REGEX = re.compile('^<a href="(https://leetcode.com/problems/.+/)">.+')


def get_solved_tasks(parent: pathlib.Path):
    solutions = parent / 'solutions'
    solved = set()
    for solution in solutions.iterdir():
        if solution.name in ['spiral_matrix_problem', 'problem_two_sum', 'roman_to_integer']:
            continue

        readme = solution / 'README.md'
        with open(readme) as f:
            line = f.readlines()[-1]
            m = REGEX.match(line)
            assert REGEX.match(line), readme
            problem = m.group(1) + '\n'
            assert problem not in solved, problem
            solved.add(problem)
    return sorted(solved)


def main():
    parent = pathlib.Path().parent
    with open(parent / 'solved_problems.txt', 'w') as f:
        f.writelines(get_solved_tasks(parent))


if __name__ == '__main__':
    main()
