#! /usr/bin/fish

if test (count $argv) -eq 1
    set -l day $argv[1]
    set -l padded_day (printf "%02d" $day)
    set -l aoc_url "https://adventofcode.com/2021/day/$day"
    curl $aoc_url > "/tmp/aoc2021d$day.html" 2> /dev/null
    mkdir -p "day$padded_day"
    pandoc --from html --to markdown "/tmp/aoc2021d$day.html" -o "day$padded_day/README.md"
else
    echo "Usage: init_day.fish 1"
end
