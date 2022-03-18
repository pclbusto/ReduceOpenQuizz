# -*- coding: utf-8 -*-
""" Template script """

import argparse
import json
import re

# -----------------------------------------------------------------------------
# Global / Functions
# -----------------------------------------------------------------------------
RE_EMPTY       = re.compile('^ *$', re.IGNORECASE)
#1.¿Cuál es el nombre del río más largo del mundo?

def _get_non_empty_lines(p_in_file):
    lines=[]
    with open(p_in_file, encoding='utf-8') as f_in:
        for line in f_in.readlines():
            line=line.strip()
            if not RE_EMPTY.match(line):
                lines.append(line)

    return lines

# 1.¿Cuál es el nombre del río más largo del mundo?
# A: Río Nilo
# B: Río Amazonas
# C: Río Danubio
# Respuesta: El río Amazonas.
def _parse_cultura_general(lines):
    re_question    = re.compile('^[0-9]* *\. *(.*)$')
    re_answer      = re.compile('^[A-Z]* *: *([^\.]+).*$')
    re_true_answer = re.compile('^Respuesta *: *([^\.]+).*$')

    data=[]

    question=None
    answers=[]
    true_answer=None
    for line in lines:
        m = re_question.match(line)
        if m:
            question=m.group(1)
            answers=[]
            true_answer=None
        else:
            m = re_true_answer.match(line)
            if m:
                true_answer=m.group(1).lower()
                if true_answer in answers:
                    answers.remove(true_answer)
                else:
                    print("ERROR : ANSWER %s not found" % (true_answer))
                data.append({
                    "q" : question,
                    "t" : true_answer,
                    "f" : answers
                })
                question=None
                answers=[]
                true_answer=None
            else:
                m = re_answer.match(line)
                if m:
                    answers.append(m.group(1).lower())
                else:
                    print("ERROR : Unknown line (%s)" % (line))

    return data

# https://ahaslides.com/es/blog/50-marvel-quiz-questions-and-answers/
# 1. ¿En qué año se estrenó la primera película de Iron Man, que lanzó el Marvel Cinematic Universe?
# 2005
# 2008
# 2010
# 2012

def _parse_marvel(lines):
    re_question    = re.compile('^[0-9]* *\. *(.*)$')
    re_answer      = re.compile('^(.*)$')
    # re_true_answer = re.compile('^Respuesta *: *([^\.]+).*$')

    data=[]

    question=None
    answers=[]
    true_answer=""
    for line in lines:
        m = re_question.match(line)
        if m:
            if question:
                data.append({
                    "q" : question,
                    "t" : true_answer,
                    "f" : answers
                })

            question=m.group(1)
            answers=[]
        else:
            m = re_answer.match(line)
            if m:
                answers.append(m.group(1))
            else:
                print("ERROR : Unknown line (%s)" % (line))

    if question:
        data.append({
            "q" : question,
            "t" : "",
            "f" : answers
        })

    return data

# https://www.beano.com/posts/the-ultimate-modern-family-trivia-quiz
def _modern_familiy(lines):
    re_question    = re.compile('^[^\.]+ *\. *(.*)$')
    re_answer      = re.compile('^(.*)$')
    re_true_answer = re.compile('^\* *([^\.]+).*$')

    data=[]

    question=None
    answers=[]
    true_answer=""
    for line in lines:
        m = re_question.match(line)
        if m:
            if question:
                data.append({
                    "q" : question,
                    "t" : true_answer,
                    "f" : answers
                })

            question=m.group(1)
            answers=[]
        else:
            m = re_true_answer.match(line)
            if m:
                true_answer=m.group(1)
            else:
                m = re_answer.match(line)
                if m:
                    answers.append(m.group(1))
                else:
                    print("ERROR : Unknown line (%s)" % (line))

    if question:
        data.append({
            "q" : question,
            "t" : true_answer,
            "f" : answers
        })

    return data

def _parse_txt(lines):
    re_question      = re.compile('^- *(.*) *$')
    re_answer    = re.compile('^([^-].*) *$')

    data=[]

    question=None
    answers=[]
    true_answer=""
    for line in lines:
        m = re_question.match(line)
        if m:
            if question:
                data.append({
                    "q" : question,
                    "t" : true_answer,
                    "f" : answers
                })

            question=m.group(1)
            true_answer=""
            answers=[]
        else:
            m = re_answer.match(line)
            if m:
                if not true_answer:
                    true_answer=m.group(1)
                else:
                    answers.append(m.group(1))
            else:
                print("ERROR : Unknown line (%s)" % (line))

    if question:
        data.append({
            "q" : question,
            "t" : true_answer,
            "f" : answers
        })

    return data

# -----------------------------------------------------------------------------
# Methods
# -----------------------------------------------------------------------------
def transform(p_in_file, p_out_file):
  
    lines=_get_non_empty_lines(p_in_file)

    # data=_parse_cultura_general(lines)
    #data=_parse_marvel(lines)
    #data=_modern_familiy(lines)
    data=_parse_txt(lines)

    with open(p_out_file, 'w', encoding='utf-8') as f_out:
        json.dump(data, f_out, indent=4, ensure_ascii=False)
        print ("File %s saved!" % (p_out_file))
  
# -----------------------------------------------------------------------------
# main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="<Help here>")

    # Actions
    # parser.add_argument('--action', action="store_true", help='<Help>')

    # Required

    # Optional
    #parser.add_argument('--in_file',  default='data/cultura_general.txt', help='<Help>')
    #parser.add_argument('--out_file',  default='cultura_general.json', help='<Help>')

    #parser.add_argument('--in_file',  default='data/marvel.txt', help='<Help>')
    #parser.add_argument('--out_file',  default='marvel.json', help='<Help>')

    parser.add_argument('--in_file',  default='data/prohibitions.txt', help='<Help>')
    parser.add_argument('--out_file',  default='out.json', help='<Help>')

    args = parser.parse_args()

    # Check parameters

    # Main
    transform(args.in_file, args.out_file)
