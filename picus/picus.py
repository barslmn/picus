#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import argparse
from picus import __version__
from picus.core.variantclassification import VariantClassification
from picus.core.evidencecollection import EvidenceCollection
from picus.utils.createreport import CreateReport
from picus import templates

import pandas as pd
import json


def get_args():
    parser = argparse.ArgumentParser()

    # Not functional
    parser.add_argument('-v', '--verbose', required=False, action='store_true',
                        help='WIP.Write what is happening to stdout.')

    parser.add_argument('--version',
                        action='version', version=__version__)

    parser.add_argument('-i', '--input', required=True,
                        default=None, type=str, help='input annotation file.')
    parser.add_argument('-o', '--output', required=False,
                        default=None, type=str, help='output annotation file.')
    parser.add_argument('-t', '--template', required=False,
                        default=os.path.join(
                            templates.__path__[0],
                            'template.Rnw'),
                        type=str,
                        help='template file')
    parser.add_argument('-l', '--logo', required=False,
                        default=os.path.join(
                            templates.__path__[0],
                            'picus.png'),
                        type=str,
                        help='custom logo')
    parser.add_argument('-r', '--report-data', required=False,
                        default=None, type=str,
                        help='custom logo')
    parser.add_argument('-c', '--command', required=False,
                        default='pdflatex', type=str,
                        help='command to run when compiling in other format')
    parser.add_argument('-g', '--group', required=False,
                        default=None, type=str,
                        help='group variants based on given parameter')
    parser.add_argument('-k', '--keep', required=False,
                        default=None, type=str,
                        help='keep intermediary file while creating report')

    if len(sys.argv[1:]) == 0:
        parser.print_help()
        parser.exit()
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    input_file = args.input
    output_file = args.output
    template = args.template
    report_data = args.report_data
    command = args.command
    group = args.group
    keep = args.keep
    variant_info_cols = [
        'CHR', 'POS', 'REF', 'ALT', 'GT', 'AD',
        'id', 'gene_symbol', 'transcript_id',
        'hgvsc', 'hgvsp',
        'transcript_consequence_terms',
        'evidences', 'significance'
    ]

    df = pd.read_csv(
        input_file,
        dtype={'CHR': 'object'},
        low_memory=False,
    )
    evidence_collector = EvidenceCollection()
    variant_classifier = VariantClassification()

    df = evidence_collector.collect_evidences(df)

    df['significance'] = df.evidences.apply(
        variant_classifier.classify_variant,
        args=(True,)
    )
    df['evidences'] = df.evidences.apply(
        evidence_collector.flat_evidences
    )

    if output_file is None:
        sys.stdout.write(
            df[variant_info_cols].to_json(orient='records')
        )
    else:
        if output_file.endswith('.csv'):
            df.to_csv(output_file, index=False)
        if output_file.endswith('.pdf'):
            variants = json.loads(
                df[variant_info_cols].to_json(orient='records'))
            reporter = CreateReport(
                variants,
                template,
                report_data,
                command,
                group,
                output_file,
                keep,
            )
            reporter.create_report()


if __name__ == '__main__':
    main()
