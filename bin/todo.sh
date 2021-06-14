grep -R -n "] TODO" . | fgrep -v deprecated | sed -e 's/^/- [ ] /'
