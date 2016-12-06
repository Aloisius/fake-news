#!/usr/bin/env python3
#
# Generates scss for reddit stylesheet
#
import re

class Pattern(object):
    MATCH_SUBSTRING = 0
    MATCH_PREFIX = 1
    MATCH_SUFFIX = 2
    MATCH_EXACT = 3
    MATCH_NONE = 4

    def __init__(self, pattern):
        self.pattern = pattern

        if pattern:
            self.match_type = self.MATCH_SUBSTRING

            if pattern.startswith('^'):
                self.match_type |= self.MATCH_PREFIX
                pattern = pattern[1:]

            if pattern.endswith('$'):
                self.match_type |= self.MATCH_SUFFIX
                pattern = pattern[:-1]
        else:
            self.match_type = self.MATCH_NONE

        self.text = pattern

    def match(self, text):
        if self.match_type == self.MATCH_SUFFIX:
            return text.endswith(self.text)
        elif self.match_type == self.MATCH_PREFIX:
            return text.startswith(self.text)
        elif self.match_type == self.MATCH_NONE:
            return True
        elif self.match_type == self.MATCH_EXACT:
            return self.text == text
        elif self.match_type == self.MATCH_SUBSTRING:
            return self.text.find(text) != -1

    def __str__(self):
        labels = ['MATCH_SUBSTRING', 'MATCH_PREFIX', 'MATCH_SUFFIX', 'MATCH_EXACT', 'MATCH_NONE']
        return '<{} {}>'.format(self.text, labels[self.match_type])


class Rule(object):
    def __init__(self, category, domain, path=None):
        self.category = category
        self.domain = Pattern(domain)
        self.path = Pattern(path)

    def match(self, domain, path):
        return self.domain.match(domain) and self.path.match(path)

    def __str__(self):
        return 'Rule<{}: {} {}>'.format(self.category, self.domain, self.path)



class RuleMatcher(object):
    def __init__(self, rules):
        self.rules = rules

    def match(self, domain, path):
        for rule in self.rules:
            if rule.match(domain, path):
                return True
        return False


def main(files):
    domain_regex = r'^\^?[a-z0-9-.]+\$?$'
    domain_re = re.compile(domain_regex)

    long_regex = r'^(\^?[a-z0-9-.]+) ([a-z0-9-./]+\$)$'
    long_re = re.compile(long_regex)

    short_regex = r'^(\^?[a-z0-9-.]+)(/[a-z0-9-./]*\$)$'
    short_re = re.compile(short_regex)

    rules = []
    for fn, category in files:
        with open(fn, 'r') as f:
            for line in f:
                line = line.strip()
                if line == '':
                    continue

                print(line)

                if line.find('#') != -1:
                    line, comment = line.rsplit('#', 1)
                    line = line.strip()
                    if line == '':
                        continue

                line = line.lower()
                if line.find(' ') != -1:
                    domain_exp, path_exp = line.split(' ', 1)
                    rules.append(Rule(category, domain_exp, path_exp))
                elif line.find('/') != -1:
                    domain_exp, path_exp = line.split('/', 1)

                    rules.append(Rule(category, domain_exp + '$', '^/' + path_exp))
                elif domain_re.match(line):
                    rules.append(Rule(category, line))
                else:
                    print("invalid line: '{}'".format(line))

    matcher = RuleMatcher(rules)
    assert matcher.match('ap.org', '/somewhere/awesome/') is True
    assert matcher.match('ap.org', '/') is True
    assert matcher.match('bigstory.ap.org', '/') is True
    assert matcher.match('nonexistant.org', '/') is False

    with open('_domains.scss', 'w') as f:
        for rule in rules:
            domainpart = []
            rulepart = ''
            if rule.domain.match_type == Pattern.MATCH_SUFFIX:
                domainpart.append('[data-domain="{}"]'.format(rule.domain.text))
                domainpart.append('[data-domain$=".{}"]'.format(rule.domain.text))
            elif rule.domain.match_type == Pattern.MATCH_EXACT:
                domainpart.append('[data-domain="{}"]'.format(rule.domain.text))
            elif rule.domain.match_type == Pattern.MATCH_PREFIX:
                domainpart.append('[data-domain^="{}"]'.format(rule.domain.text))
            elif rule.domain.match_type == Pattern.MATCH_SUBSTRING:
                domainpart.append('[data-domain*="{}"]'.format(rule.domain.text))

            if rule.path.match_type == Pattern.MATCH_SUFFIX:
                rulepart = '[data-url$="{}"]'.format(rule.path.text)
            elif rule.path.match_type == Pattern.MATCH_SUFFIX and rule.domain.match_type in (Pattern.MATCH_SUFFIX, Pattern.MATCH_EXACT):
                rulepart = '[data-url$="{}{}"]'.format(rule.domain.text, rule.path.text)
            elif rule.path.match_type == Pattern.MATCH_PREFIX and rule.domain.match_type in (Pattern.MATCH_SUFFIX, Pattern.MATCH_EXACT):
                rulepart = '[data-url*="{}{}"]'.format(rule.domain.text, rule.path.text)
            elif rule.path.match_type in (Pattern.MATCH_PREFIX, Pattern.MATCH_SUBSTRING, Pattern.MATCH_EXACT):
                rulepart = '[data-url*="{}"]'.format(rule.path.text)

            if rulepart or len(domainpart):
                if len(domainpart):
                    for domain in domainpart:
                        o='''
                        div.link{} div.entry p.title::before {{
                          @extend %{};
                        }}
                        '''
                        f.write(o.format(domain+rulepart, rule.category))
                else:
                    o='''
                    div.link{} div.entry p.title::before {{
                      @extend %{};
                    }}
                    '''
                    f.write(o.format(rulepart, rule.category))
            else:
                print("unsupported rule format {}".format(rule))



if __name__ == "__main__":
    files = [
        ('../lists/fakenews-aloisius.txt', 'fringe'),
        ('../lists/fakenews-snopes.txt', 'fringe'),
        ('../lists/fakenews-zidmars.txt', 'fringe'),
        ('../lists/pulitzer-aloisius.txt', 'pulitzer'),
        ('../lists/opinion-aloisius.txt', 'opinion'),
    ]
    main(files)
