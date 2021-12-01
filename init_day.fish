#! /usr/bin/fish

if test (count $argv) -eq 1
    set -l day $argv[1]
    set -l padded_day (printf "%02d" $day)
    mkdir -p "day$padded_day"
    pandoc --from html --to markdown "~/Downloads/Day $day - Advent of Code 2021.html" -o "day$padded_day/README.md"
    rm "~/Downloads/Day $day - Advent of Code 2021.html"
else
    echo "Usage: init_day.fish 1"
end
