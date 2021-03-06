# Picus
Pointed Interpretation of Clinical Variant Significance

## Quick Install
* Linux&Mac

> sudo pip3 install picus

* Windows

> pip install picus

## Example Uses

* Picus examples

> picus -i input.csv -o output.json


## Evidence Collection Process

### PVS1
* PVS1 null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multiexon deletion) in a gene where LOF is a known mechanism of disease.

#### Status
* Implemented

#### Resources
* LoF genes list from intervar. https://raw.githubusercontent.com/barslmn/InterVar/master/intervardb/PVS1.LOF.genes.hg19
* Null variants defined as HIGH IMPACT by https://www.ensembl.org/info/genome/variation/prediction/predicted_data.html

#### Conditions
* "gene_symbol" is in LoF gene list.
* "transcript_consequence_terms" is high impact.

#### Shortcomings
* LoF gene list is only predictive and may be missing some actual LoF genes.
* No checks for multiexon deletion.

### PS1
* Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

#### Status
* Implemented

#### Resources
* Clinvar xml (ftp://ftp.ncbi.nlm.nih.gov/pub/clinvar/)

#### Annotation Steps
1. Clinvar data is parsed using https://github.com/barslmn/clinvar.
2. Sample data and clinvar data is merged based on columns "CHR" and "POS".
3. Clinvar feature columns "ALT", "hgvsp", and "clinical_significance" added to original annotation.

#### Conditions
1. "clinical_significance" is pathogenic.
2. Sample "hgvsp" and later added clinvar "hgvsp" changes are the same.
3. Sample "ALT" and clinvar "ALT" are different.

#### Shortcomings

### PS2
* De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

#### Status
* Not Checked

#### Resources

#### Conditions

#### Shortcomings

### PS3
* Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product

#### Status
* Not Checked

#### Resources

#### Conditions

#### Shortcomings

### PS4
* The prevalence of the variant in affected individuals is significantly increased compared with the prevalence in controls

#### Status
* Implemented

#### Resources
* Intervar

#### Conditions
1. "id" is in id list.

#### Shortcomings
1. No idea how the source is made.

### PM1
* Located in a mutational hot spot and/or critical and well-established functional domain (e.g., active site of an enzyme) without benign variation

#### Status
* Planned.

#### Resources

#### Conditions

#### Shortcomings

### PM2
* Absent from controls (or at extremely low frequency if recessive) (Table 6) in Exome Sequencing Project, 1000 Genomes Project, or Exome Aggregation Consortium

#### Status
* Implemented

#### Resources
* VEP

#### Conditions
* "gnomad" less than 0.001.

#### Shortcomings

### PM3
* For recessive disorders, detected in trans with a pathogenic variant

#### Status
* Planned for trio

#### Resources

#### Conditions

#### Shortcomings

### PM4
* Protein length changes as a result of in-frame deletions/insertions in a nonrepeat region or stop-loss variants

#### Status
* Implemented

#### Resources
* VEP

#### Conditions
* "transcript_consequence_terms" is "inframe_insertion", "inframe_deletion", or "stop_lost".

#### Shortcomings
* No checks for repeat regions.

### PM5
* Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before

#### Status
* Broken. (╯°□°）╯︵ ┻━┻)

#### Resources
* Clinvar xml (ftp://ftp.ncbi.nlm.nih.gov/pub/clinvar/)

#### Annotation Steps
1. Clinvar data is parsed using https://github.com/barslmn/clinvar.
2. Sample data and clinvar data hgvsp columns parsed till position.
3. Synonym changes removed from clinvar data.
4. Clinvar feature columns "hgvsc", and "clinical_significance" added to original annotation based on protein change position.

#### Conditions
1. "gnomad" less then 0.001.
2. "clinical_significance" is pathogenic.
3. "transcript_consequence_terms" is missense variant.
4. "hgvsc" of the variant and clinvar entry dont match.

#### Shortcomings

### PM6
* Assumed de novo, but without confirmation of paternity and maternity

#### Status
* Planned for trio.

#### Resources

#### Conditions

#### Shortcomings

### PP1
* Cosegregation with disease in multiple affected family members in a gene definitively known to cause the disease

#### Status
* Planned after Vesta.

#### Resources

#### Conditions

#### Shortcomings

### PP2
* Missense variant in a gene that has a low rate of benign missense variation and in which missense variants are a common mechanism of disease

#### Status
* Implemented

#### Resources
* Intervar

#### Conditions
* "transcript_consequence_terms" is a missense variant.
* "gene_symbol" is in PP2 gene list.

#### Shortcomings

### PP3
* Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.)

#### Status
* Implemented

#### Resources
* Vep

#### Conditions
* "sift_score" less than 0.05
* "polyphen_score" greater than 0.908

#### Shortcomings

### PP4
* Patient’s phenotype or family history is highly specific for a disease with a single genetic etiology

#### Status
* Not Checked.

#### Resources

#### Conditions

#### Shortcomings

### PP5
* Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation

#### Status
* Implemented.

#### Resources
* Clinvar

#### Conditions
* "clinical_significance" is Pathogenic.

#### Shortcomings

### Benign

### BA1
* Allele frequency is >5% in Exome Sequencing Project, 1000 Genomes Project, or Exome Aggregation Consortium

#### Status
* Implemented.

#### Resources
* Vep

#### Conditions
* "minor_allele_freq" is greater than 0.05

OR

* "gnomad" is greater than 0.05.

#### Shortcomings

### BS1
* Allele frequency is greater than expected for disorder

#### Status
* Planned for later.

#### Resources

#### Conditions

#### Shortcomings

### BS2
* Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age

#### Status
* Planned

#### Resources
* Intervar

#### Conditions

#### Shortcomings

### BS3
* Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing

#### Status
* Not Checked.

#### Resources

#### Conditions

#### Shortcomings

### BS4
* Lack of segregation in affected members of a family

#### Status
* Not Checked.

#### Resources

#### Conditions

#### Shortcomings

### BP1
* Missense variant in a gene for which primarily truncating variants are known to cause disease

#### Status
* Implemented.

#### Resources
* Intervar

#### Conditions
* "transcript_consequence_terms" is a missense variant.
* "gene_symbol" is in BP1 gene list.

#### Shortcomings

### BP2
* Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern

#### Status
* Planned for trio.

#### Resources

#### Conditions

#### Shortcomings

### BP3
* In-frame deletions/insertions in a repetitive region without a known function

#### Status
* Not Checked.

#### Resources

#### Conditions

#### Shortcomings

### BP4
* Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc.)

#### Status
* Implemented

#### Resources
* VEP

#### Conditions
* "sift_score" greater than or equals to 0.05
* "polyphen_score" less than or equals to 0.446

#### Shortcomings

### BP5
* Variant found in a case with an alternate molecular basis for disease

#### Status
* Not Checked.

#### Resources

#### Conditions

#### Shortcomings

### BP6
* Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation

#### Status
* Implemented

#### Resources
* Clinvar

#### Conditions
* "clinical_significance" is benign

#### Shortcomings

### BP7
* A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved

#### Status
* Planned

#### Resources

#### Conditions

#### Shortcomings
