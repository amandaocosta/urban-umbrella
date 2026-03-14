# Comprehensive Analysis — All 39 Transaction Codes
## Manual Journal Entries vs. Automatic Postings — Nubank SAP Financial Accounting

**Document Status:** FINAL — Approved for Distribution  
**Prepared by:** Amanda O. Costa  
**Date:** 2026-03-11  
**Distribution:** Controllership Director | SOX Team  
**Source Data:** New_Query_2026_02_25_16_33_43 (1).csv — 11,008,486 total posting lines

---

## Overview

This document provides a complete, code-by-code analysis of all **39 named SAP transaction codes** identified in the production data. Each code is classified as Manual or Automatic based on the three core criteria defined in `FINAL_Classification_Criteria_Definition.md`:

1. The `movement_type` field in the source data (`manual` / `automatic`)
2. The design intent of the transaction code (discretionary posting vs. rule-based automated processing)
3. The creator user identity (individual named person vs. system/batch account)

**Population note:** An additional 3,525,012 posting lines appear in the data with a **blank** transaction code field. These are all classified as `automatic` and are produced by system accounts (LAMBDA_PNU_P, SAPCPI, USERJOB, KBRIGHI, LCAMARGO) generating document types AA, CC, ES, HR, KR, KS, SC, TX, YA, YB, YC, YD, YI, YL, YM, YN, YP, YX. They are excluded from the 39-code analysis but noted here for completeness.

---

## Summary — Classification Results

### Manual Journal Entry Transaction Codes (3 codes)

| # | Transaction Code | Manual Lines | Auto Lines | Manual % | Primary Document Types |
|---|---|---|---|---|---|
| 1 | **FBDC_P001** | 1,074,437 | 4,784 | 99.6% | SA, CP, FP, PR, RF, GO, TX, SR, FI, IC, BK, N1, VC, CR, CS, ZR, YX |
| 2 | **ZFI_ADP** | 380,618 | 0 | 100.0% | FP |
| 3 | **FBD5** | 572 | 0 | 100.0% | GO, SA |
| | **TOTAL** | **1,455,627** | **4,784** | **99.7%** | |

### Automatic Posting Transaction Codes (36 codes)

| # | Transaction Code | Auto Lines | Manual Lines | Auto % | Primary Document Types |
|---|---|---|---|---|---|
| 1 | FB01 | 2,568,096 | 0 | 100.0% | ZR, TI |
| 2 | KSV5 | 976,500 | 0 | 100.0% | CO, CS |
| 3 | AFABN | 449,724 | 0 | 100.0% | AF |
| 4 | FAGL_IT_02 | 1,222,444 | 5,468 | 99.6% | EC, N1 |
| 5 | F110 | 195,049 | 0 | 100.0% | ZP, SU |
| 6 | FB08 | 313,294 | 3,788 | 98.8% | ES, FP, IC, N1 |
| 7 | FBB1 | 72,186 | 630 | 99.1% | SU, FI, SA, VC, YH |
| 8 | MIRO | 93,674 | 2 | 99.9% | AA, KR, RE, SR |
| 9 | KO8G | 44,918 | 0 | 100.0% | AA, ES |
| 10 | FBVB | 19,190 | 0 | 100.0% | KR, KS |
| 11 | LSMW | 16,496 | 0 | 100.0% | AA |
| 12 | FB05 | 9,737 | 0 | 100.0% | KR, KZ, TI, ZR |
| 13 | F111 | 7,414 | 0 | 100.0% | ZP, ZR, ZV |
| 14 | AB08 | 5,335 | 0 | 100.0% | ES |
| 15 | FBDC_C014 | 4,884 | 0 | 100.0% | KZ, ZP |
| 16 | ABUMN | 3,660 | 0 | 100.0% | AA |
| 17 | FBZ2 | 3,823 | 0 | 100.0% | KZ |
| 18 | ABZON | 1,214 | 0 | 100.0% | AA, AF |
| 19 | FB1K | 1,513 | 0 | 100.0% | SU |
| 20 | FB1S | 1,017 | 0 | 100.0% | SU |
| 21 | ABAVN | 371 | 0 | 100.0% | AA |
| 22 | ZLIA_COCKPIT | 406 | 0 | 100.0% | AA |
| 23 | FBDC_C024 | 395 | 0 | 100.0% | KZ |
| 24 | MR8M | 226 | 0 | 100.0% | AA, RE |
| 25 | KO88 | 206 | 0 | 100.0% | AA, ES |
| 26 | MIR4 | 140 | 0 | 100.0% | AA |
| 27 | FBL1N | 103 | 0 | 100.0% | ES |
| 28 | FV60 | 102 | 0 | 100.0% | KG |
| 29 | FB70 | 72 | 0 | 100.0% | DR |
| 30 | FBA7 | 38 | 0 | 100.0% | KZ, SU |
| 31 | FBDC_C080 | 82 | 0 | 100.0% | ZR |
| 32 | ZMM_CARGA_MIRO_MX | 18 | 0 | 100.0% | AA |
| 33 | FBDC_C002 | 683 | 0 | 100.0% | SU |
| 34 | FBDC_C022 | 155 | 0 | 100.0% | DZ, SU |
| 35 | AS02 | 4 | 0 | 100.0% | AA |
| 36 | AB01L | 6 | 0 | 100.0% | AA |
| | **TOTAL** | **6,017,959** | **9,888** | **99.8%** | |

---

## Detailed Analysis — Each Transaction Code

### MANUAL JOURNAL ENTRY CODES

---

#### 1. FBDC_P001 — Manual Posting Module (Primary)

| Attribute | Value |
|---|---|
| **Classification** | 🔴 MANUAL JOURNAL ENTRY |
| **Manual posting lines** | 1,074,437 (99.6%) |
| **Automatic posting lines** | 4,784 (0.4%) |
| **Total posting lines** | 1,079,221 |
| **Document types** | SA, CP, FP, PR, RF, GO, TX, SR, FI, IC, BK, N1, VC, CR, CS, ZR, YX |
| **System users present** | None |
| **Representative human users** | DFERREIRA, HBALBINO, FSOUZA, JEPEREIRA, SBORECKI, AMALMEIDA, KCORREA, NCAMACHO, PSAMPAIO, BVALIATE, AROCHA, ACOUTINHO, LSINIBALDI |

**SAP Description:** FBDC_P001 is Nubank's primary manual General Ledger posting screen. It is a custom transaction built on top of the standard SAP FB01/FBD1 framework, specifically configured for manual journal entry submission with an embedded approval workflow. All postings through this code require individual user authentication, business justification, and supervisory approval before the document is posted to the GL.

**Why classified as MANUAL:**
- 99.6% of lines carry `movement_type = "manual"` in the source data
- No system/batch accounts (LAMBDA_PNU_P, SAPCPI, USERJOB) post through this code — exclusively human users
- The document type range (SA, CP, PR, RF, GO, TX, SR, FI, IC, BK, etc.) represents discretionary accounting decisions: consolidation postings, tax adjustments, FX revaluations, intercompany entries, and bank adjustments — all requiring accountant judgment
- The 0.4% automatic lines (4,784) are technical workflow-triggered reversals or batch-generated support documents; the primary posting intent remains manual

**SOX implications:** Highest risk MJE transaction code by volume. All entries through FBDC_P001 must be included in the MJE population for SOX testing. Approval evidence should be retained for each document.

---

#### 2. ZFI_ADP — Manual Financial Adjustments (ADP Integration)

| Attribute | Value |
|---|---|
| **Classification** | 🔴 MANUAL JOURNAL ENTRY |
| **Manual posting lines** | 380,618 (100.0%) |
| **Automatic posting lines** | 0 |
| **Total posting lines** | 380,618 |
| **Document types** | FP |
| **System users present** | None |
| **Representative human users** | HBALBINO, JEPEREIRA |

**SAP Description:** ZFI_ADP is a custom Nubank transaction code used by the payroll/ADP integration team to post financial adjustments related to payroll and compensation accounting. Despite the integration context, all postings require individual user initiation (HBALBINO, JEPEREIRA) and are recorded as manual.

**Why classified as MANUAL:**
- 100% of lines carry `movement_type = "manual"` — zero automatic postings
- Exclusively two named individual users; no system/batch accounts
- Document type FP (Financial Posting / Invoice) indicates a discretionary financial adjustment rather than a workflow-generated document
- The restricted user base (only two individuals) suggests this is a privileged, high-accountability manual posting path

**SOX implications:** Although posted by only two users, the volume (380,618 lines) is significant. The restricted access profile increases risk of concentration — segregation of duties should be verified to ensure the preparer is not also the approver.

---

#### 3. FBD5 — Manual Reversal / Recurring Entry Posting

| Attribute | Value |
|---|---|
| **Classification** | 🔴 MANUAL JOURNAL ENTRY |
| **Manual posting lines** | 572 (100.0%) |
| **Automatic posting lines** | 0 |
| **Total posting lines** | 572 |
| **Document types** | GO, SA |
| **System users present** | None |
| **Representative human users** | CALCANTARA, ISOUZA, MREIS |

**SAP Description:** FBD5 (Post Recurring Entry) is the standard SAP transaction for manually triggering the posting of pre-configured recurring journal entries and executing manual reversals. Each execution requires individual user action and authorization.

**Why classified as MANUAL:**
- 100% of lines carry `movement_type = "manual"`
- Three named accountants only; no system accounts
- Document types GO (Goods Issue / General Adjustment) and SA (G/L Account Document) represent period-end manual adjustments
- As a reversal/recurring entry tool, each use represents a deliberate accounting decision

**SOX implications:** Lower volume but 100% manual. Recurring entries created through FBD5 should be reviewed at period-end to confirm continued business validity. All reversals should reference the original document being reversed.

---

### AUTOMATIC POSTING CODES

---

#### 4. FB01 — Standard Document Entry / Automated Receivables

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 2,568,096 (100.0%) |
| **Manual posting lines** | 0 |
| **Total posting lines** | 2,568,096 |
| **Document types** | ZR (Automatic Receivables), TI (Technical Routine Posting) |
| **System users present** | USERJOB |
| **Representative human users** | ANAVARRO, APATARROYO, DACASTRO, EBAZBAZ, FAGUIRRE, FSAMPAIO, GABLIMA |

**SAP Description:** FB01 is the standard SAP document entry transaction. At Nubank, it is used overwhelmingly in automated batch mode (USERJOB) to post high-volume receivables (ZR) and technical postings (TI). When human users appear, they are triggering automated workflows rather than making discretionary entries.

**Why classified as AUTOMATIC:** 100% automatic movement_type. The ZR document type is a system-assigned receivables posting type that cannot be created through a discretionary manual entry path. The presence of USERJOB confirms batch processing.

---

#### 5. KSV5 — Cost Center Distribution / Automatic Clearing

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 976,500 (100.0%) |
| **Manual posting lines** | 0 |
| **Total posting lines** | 976,500 |
| **Document types** | CO (Controlling Document), CS (Cost Sharing) |
| **System users present** | None |
| **Representative human users** | AMALMEIDA, DFERREIRA, JCAMPOS, MCOLOZZO, SBORECKI, TGONZALEZ |

**SAP Description:** KSV5 executes cost center distributions and assessments in SAP Controlling. It applies pre-configured distribution rules across cost centers automatically. Human users trigger the execution, but the posting itself follows deterministic rules set in configuration — there is no discretion at runtime.

**Why classified as AUTOMATIC:** 100% automatic movement_type. The execution of KSV5 applies a pre-approved configuration — the human action is to initiate the run, not to determine the accounting entries. CO/CS document types are controlling documents, not GL journal entries requiring approval.

---

#### 6. AFABN — Asset Depreciation Posting (Batch)

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 449,724 (100.0%) |
| **Manual posting lines** | 0 |
| **Total posting lines** | 449,724 |
| **Document types** | AF (Asset Depreciation) |
| **System users present** | USERJOB |
| **Representative human users** | DFERREIRA, EVALADEZ, FMUNOZ, LPUERTO, MCOLOZZO, NMOLINA, RCASTILLO |

**SAP Description:** AFABN (or AFAB — Asset Depreciation Run) posts period-end depreciation for the fixed asset subledger. The calculation method, useful life, and accounts are all configured in the Asset Master and depreciation key. USERJOB executes the periodic run automatically.

**Why classified as AUTOMATIC:** Depreciation is entirely rules-based. No human judgment determines the amount or account at the time of posting. USERJOB confirms the batch nature. AF document type is exclusively system-generated.

---

#### 7. FAGL_IT_02 — GL Intercompany / Electronic Clearing

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING (with minor manual exceptions) |
| **Automatic posting lines** | 1,222,444 (99.6%) |
| **Manual posting lines** | 5,468 (0.4%) |
| **Total posting lines** | 1,227,912 |
| **Document types** | EC (Electronic Clearing), N1 (Credit Memo / Non-standard Adjustment) |
| **System users present** | None |
| **Representative human users** | CAARAUJO, DABE, DCARIUS, FRUIZ, TCOELHO, UTEIXEIRA |

**SAP Description:** FAGL_IT_02 is used for GL intercompany account maintenance and electronic clearing. The overwhelming majority of activity is automated clearing (EC). The small manual subset (N1 documents, 5,468 lines) represents manual credit memo adjustments processed by the GL team.

**Why classified as AUTOMATIC (with exception):** 99.6% automatic. The 5,468 manual lines (N1 document type) represent a minor manual exception population. **For SOX purposes, the N1/manual subset from FAGL_IT_02 should be included in the MJE population**, even though the code is predominantly automatic.

**SOX note:** Extract `movement_type = "manual"` AND `erp_transaction_code = "FAGL_IT_02"` as a supplementary MJE population (5,468 lines).

---

#### 8. F110 — Automatic Payment Program

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 195,049 (100.0%) |
| **Manual posting lines** | 0 |
| **Total posting lines** | 195,049 |
| **Document types** | ZP (Automatic Payment), SU (Standard Utility) |
| **System users present** | USERJOB |
| **Representative human users** | ALARAUJO, CALVAREZ, DCOSTO, EBAZBAZ, FAGUIRRE, FSAMPAIO, GCIBOTTO |

**SAP Description:** F110 is the SAP Automatic Payment Program — the standard tool for generating and posting vendor and customer payments in batch. Payment proposals are reviewed by human users, but the actual posting is executed by USERJOB through automated payment runs.

**Why classified as AUTOMATIC:** ZP and SU document types are exclusively generated by F110 in payment run mode. USERJOB confirms batch execution. Human involvement is in configuring and approving the payment proposal — the posting itself is automated.

---

#### 9. FB08 — Reverse Document / Standard Posting

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING (with minor manual exceptions) |
| **Automatic posting lines** | 313,294 (98.8%) |
| **Manual posting lines** | 3,788 (1.2%) |
| **Total posting lines** | 317,082 |
| **Document types** | ES (Standard Posting), FP (Financial Posting), IC (Intercompany), N1 (Credit Memo) |
| **System users present** | USERJOB |
| **Representative human users** | AAGUIAR, ACOUTINHO, ADOMINGUEZ, ALARAUJO, ALMARQUES, AMALMEIDA |

**SAP Description:** FB08 reverses previously posted documents. The majority of reversals are system-triggered (USERJOB). The small manual subset reflects individual accountants reversing specific documents as an exception.

**Why classified as AUTOMATIC (with exception):** 98.8% automatic. The 3,788 manual lines should be included in the MJE population for SOX testing.

**SOX note:** Extract `movement_type = "manual"` AND `erp_transaction_code = "FB08"` as a supplementary MJE population (3,788 lines).

---

#### 10. FBB1 — Bank Accounting / Misc. GL Transactions

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING (with minor manual exceptions) |
| **Automatic posting lines** | 72,186 (99.1%) |
| **Manual posting lines** | 630 (0.9%) |
| **Total posting lines** | 72,816 |
| **Document types** | SU, FI (Financial), SA (G/L Account), VC (Vendor/Customer Adj.), YH |
| **System users present** | USERJOB |
| **Representative human users** | AOSORIO, APEREZ, ARAMIREZ, ARFRIAS, AROCHA, BALVES, FERUIZ |

**SAP Description:** FBB1 handles bank accounting entries and miscellaneous GL transactions. The automated majority processes standard banking transactions. The manual subset includes individual accountants processing FI, SA, and VC document types — financial adjustments, G/L entries, and vendor/customer corrections.

**Why classified as AUTOMATIC (with exception):** 99.1% automatic. The 630 manual lines should be included in the MJE population.

**SOX note:** Extract `movement_type = "manual"` AND `erp_transaction_code = "FBB1"` as a supplementary MJE population (630 lines).

---

#### 11. MIRO — Logistics Invoice Verification

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 93,674 (99.9%) |
| **Manual posting lines** | 2 (0.0%) |
| **Total posting lines** | 93,676 |
| **Document types** | AA (Automatic Accounting), KR (Vendor Invoice), RE (Invoice Receipt), SR (System Reversal) |
| **System users present** | SAPCPI |
| **Representative human users** | CALVAREZ, DALVES, IRANGEL, ISOUZA, JTOCANCHON, MOLIVEIRA, MREIS, NSANTOS |

**SAP Description:** MIRO (Logistics Invoice Verification) posts vendor invoices against purchase orders. SAPCPI automates the three-way match (PO, GR, invoice). Human users process exceptions. The 2 manual lines are effectively immaterial rounding/exception entries.

**Why classified as AUTOMATIC:** 99.9% automatic. The 2 manual lines are immaterial and may be treated as exceptions rather than a distinct manual population.

---

#### 12. KO8G / KO88 — Internal Order Settlement

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **KO8G automatic posting lines** | 44,918 |
| **KO88 automatic posting lines** | 206 |
| **Manual posting lines** | 0 |
| **Document types** | AA (Automatic Accounting), ES (Standard Posting) |
| **System users present** | None |
| **Representative human users** | DFERREIRA, MCOLOZZO |

**SAP Description:** KO8G and KO88 settle internal orders — transferring costs from internal orders to cost centers, assets, or GL accounts based on pre-configured settlement rules. Execution is deterministic, rule-based, and requires no accounting judgment.

**Why classified as AUTOMATIC:** 100% automatic. Settlement rules are pre-configured; human users trigger the batch run, not the individual accounting entries.

---

#### 13. FBVB — Post Parked Document (Workflow)

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 19,190 (100.0%) |
| **Manual posting lines** | 0 |
| **Document types** | KR (Vendor Invoice), KS (Vendor Credit) |
| **System users present** | SAP_WFRT |
| **Representative human users** | None |

**SAP Description:** FBVB posts parked documents (documents awaiting final posting, often in the AP process). All postings are executed by SAP_WFRT — the SAP Workflow Runtime — confirming these are workflow-triggered automatic postings, not manual entries.

**Why classified as AUTOMATIC:** Exclusively SAP_WFRT (a system account). No human users. Vendor invoice and credit documents (KR, KS) are posted by the workflow upon approval completion — this is a system-automated release, not a manual journal entry.

---

#### 14. LSMW — Legacy System Migration Workbench

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 16,496 (100.0%) |
| **Manual posting lines** | 0 |
| **Document types** | AA (Automatic Accounting) |
| **System users present** | None |
| **Representative human users** | KBRIGHI, LCAMARGO |

**SAP Description:** LSMW migrates and loads data from legacy systems or external files into SAP in batch. It executes pre-configured mapping rules and posts AA (Automatic Accounting) documents. While human users execute the migration jobs, the posting logic is entirely automated.

**Why classified as AUTOMATIC:** 100% automatic. AA document type confirms system-generated postings. LSMW data loads are governed by configuration and migration scripts, not individual accounting judgment.

---

#### 15. FB05 — Post with Clearing

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 9,737 (100.0%) |
| **Manual posting lines** | 0 |
| **Document types** | KR, KZ (Payment Clearing), TI (Technical), ZR (Automatic Receivables) |
| **System users present** | None |
| **Representative human users** | ARFRIAS, DALVES, DCOSTO, IRANGEL, ISOUZA, KPLAZA, MOLIVEIRA, MREIS |

**SAP Description:** FB05 posts documents with simultaneous clearing of open items. The clearing process matches debits and credits per configured tolerances. The resulting document types (KR, KZ, TI, ZR) are all system-assigned clearing types.

**Why classified as AUTOMATIC:** 100% automatic. Clearing rules are configured; human users may initiate, but the accounting determination is system-driven.

---

#### 16. F111 — Payment Order Processing

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 7,414 (100.0%) |
| **Manual posting lines** | 0 |
| **Document types** | ZP (Automatic Payment), ZR (Automatic Receivables), ZV (Automatic Valuation) |
| **System users present** | CASHMGTBR |
| **Representative human users** | APATARROYO, CASHMGTBR-related, DACASTRO, FAGUIRRE, FSAMPAIO |

**SAP Description:** F111 processes payment orders and cash management postings. CASHMGTBR (Cash Management System — Brazil) is a system account that drives the automated cash position postings. ZP, ZR, and ZV document types are exclusively system-generated.

**Why classified as AUTOMATIC:** CASHMGTBR is a system account. ZP/ZR/ZV document types are automatic. 100% automatic movement_type.

---

#### 17. AB08 — Reverse Asset Document

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 5,335 (100.0%) |
| **Manual posting lines** | 0 |
| **Document types** | ES (Standard Posting) |
| **System users present** | None |
| **Representative human users** | DFERREIRA, FMUNOZ, KBRIGHI, LCAMARGO, MCOLOZZO, MVITORIA, NMOLINA |

**SAP Description:** AB08 reverses asset accounting documents. Despite human users triggering the transaction, asset reversals follow deterministic rules in the Asset Subledger — amounts and accounts are system-determined by the original document.

**Why classified as AUTOMATIC:** 100% automatic. Asset subledger postings (even reversals) are calculated and posted by the system per the original document's data.

---

#### 18. FBDC_C014 — Automated Clearing (Custom)

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 4,884 (100.0%) |
| **Manual posting lines** | 0 |
| **Document types** | KZ (Payment Clearing), ZP (Automatic Payment) |
| **System users present** | None |
| **Representative human users** | IRANGEL, ISOUZA, NSANTOS, VGRACIANO |

**SAP Description:** FBDC_C014 is a custom Nubank clearing transaction. KZ and ZP document types confirm it processes automated payment clearing and reconciliation.

**Why classified as AUTOMATIC:** 100% automatic. Document types KZ and ZP are system-assigned clearing categories; no manual override is possible.

---

#### 19. ABUMN — Transfer Within Company Code (Asset)

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 3,660 (100.0%) |
| **Manual posting lines** | 0 |
| **Document types** | AA (Automatic Accounting) |
| **System users present** | None |
| **Representative human users** | DFERREIRA, ESANTIAGO, KBRIGHI, MVITORIA |

**SAP Description:** ABUMN transfers fixed assets between asset classes or cost centers within a company code. The accounting entries (AA document type) are fully system-determined by the asset master data.

**Why classified as AUTOMATIC:** 100% automatic. AA document type is system-generated. Asset transfer amounts and accounts are determined by the system from asset master data.

---

#### 20. FBZ2 — Post Outgoing Payments

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 3,823 (100.0%) |
| **Manual posting lines** | 0 |
| **Document types** | KZ (Payment Clearing) |
| **System users present** | None |
| **Representative human users** | ARFRIAS, CALVAREZ, DCOSTO, FAGUIRRE, IRANGEL, ISOUZA, JTOCANCHON, KCORREA, LLOPEZ |

**SAP Description:** FBZ2 posts outgoing payments manually in form, but at Nubank the KZ document type indicates the payments are part of a clearing batch — the accounting determination is system-driven.

**Why classified as AUTOMATIC:** 100% automatic. KZ (payment clearing) is automatically determined by the system.

---

#### 21. FBDC_C002 — Custom Automated Utility Posting

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 683 (100.0%) |
| **Document types** | SU (Standard Utility) |
| **Representative human users** | DFORIGUA, GSARAY, SARIZA |

**Why classified as AUTOMATIC:** 100% automatic. SU (Standard Utility) documents are routine, rule-based postings.

---

#### 22. ABZON — Asset Posting (Subsequent Acquisition)

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 1,214 (100.0%) |
| **Document types** | AA (Automatic Accounting), AF (Asset Depreciation) |
| **Representative human users** | AMALMEIDA, DFERREIRA, ESANTIAGO, EVALADEZ, FMUNOZ, LPUERTO, MCOLOZZO, MVITORIA |

**Why classified as AUTOMATIC:** 100% automatic. Subledger asset postings (AA, AF) are system-determined.

---

#### 23. FB1K — Customer Invoice Posting

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 1,513 (100.0%) |
| **Document types** | SU (Standard Utility) |
| **Representative human users** | BBENITEZ, CALVAREZ, DALVES, DCOSTO, EBOTELLO, IRANGEL, ISOUZA, JTOCANCHON, MOLIVEIRA |

**Why classified as AUTOMATIC:** 100% automatic. SU document type confirms routine, rule-based posting.

---

#### 24. FB1S — Customer Credit Memo Posting

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 1,017 (100.0%) |
| **Document types** | SU (Standard Utility) |
| **Representative human users** | KCORREA, LLOPEZ |

**Why classified as AUTOMATIC:** 100% automatic. SU document type confirms routine posting.

---

#### 25. ABAVN — Asset Retirement by Scrapping

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 371 (100.0%) |
| **Document types** | AA (Automatic Accounting) |
| **Representative human users** | ALIRA, DFERREIRA, ESANTIAGO, EVALADEZ, FMUNOZ, MCOLOZZO, MVITORIA, SBORECKI |

**Why classified as AUTOMATIC:** 100% automatic. Asset retirement entries (AA) are fully system-determined from asset master data.

---

#### 26. ZLIA_COCKPIT — Automated Dashboard Operations

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 406 (100.0%) |
| **Document types** | AA (Automatic Accounting) |
| **Representative human users** | DALVES, IRANGEL, ISOUZA, MREIS, NSANTOS |

**SAP Description:** ZLIA_COCKPIT is a custom Nubank transaction providing a monitoring and operations cockpit. Postings (AA document type) are system-generated from the cockpit's automated processes.

**Why classified as AUTOMATIC:** 100% automatic. AA document type confirms system-generated entries.

---

#### 27. FBDC_C024 — Custom Clearing Transaction

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 395 (100.0%) |
| **Document types** | KZ (Payment Clearing) |
| **Representative human users** | CALVAREZ, JTOCANCHON |

**Why classified as AUTOMATIC:** 100% automatic. KZ clearing document type is system-assigned.

---

#### 28. MR8M — Cancel Invoice Document

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 226 (100.0%) |
| **Document types** | AA (Automatic Accounting), RE (Invoice Receipt) |
| **System users present** | SAPCPI |
| **Representative human users** | DALVES, MOLIVEIRA, MREIS, NSANTOS |

**SAP Description:** MR8M cancels (reverses) previously posted logistics invoices. SAPCPI automates the cancellation. The reversed document amounts are system-retrieved; no accounting judgment is required.

**Why classified as AUTOMATIC:** 100% automatic. SAPCPI confirms system automation. AA and RE document types are system-generated.

---

#### 29. KO88 — Actual Settlement: Internal Order

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 206 (100.0%) |
| **Document types** | AA (Automatic Accounting), ES (Standard Posting) |
| **Representative human users** | DFERREIRA |

**Why classified as AUTOMATIC:** 100% automatic. Internal order settlement follows configured settlement rules; no discretion at runtime.

---

#### 30. MIR4 — Display / Change Invoice Document

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 140 (100.0%) |
| **Document types** | AA (Automatic Accounting) |
| **Representative human users** | CALVAREZ, DALVES, IRANGEL, ISOUZA, MREIS, NSANTOS |

**Why classified as AUTOMATIC:** 100% automatic. MIR4 is primarily a display transaction; any postings triggered are system-generated.

---

#### 31. FBL1N — Vendor Line Item Display

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 103 (100.0%) |
| **Document types** | ES (Standard Posting) |
| **Representative human users** | CALVAREZ, IRANGEL, JTOCANCHON, NSANTOS, OSOSA |

**Why classified as AUTOMATIC:** 100% automatic. FBL1N is primarily a reporting/display transaction; system-generated standard postings only.

---

#### 32. FV60 — Park Incoming Invoice

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 102 (100.0%) |
| **Document types** | KG (Vendor Credit) |
| **Representative human users** | CALVAREZ, JTOCANCHON |

**Why classified as AUTOMATIC:** 100% automatic. Parked documents posted via FV60 generate KG (vendor credit) documents through the automated AP workflow.

---

#### 33. FBDC_C080 — Custom Automated Receivables Posting

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 82 (100.0%) |
| **Document types** | ZR (Automatic Receivables) |
| **Representative human users** | APATARROYO, DACASTRO, FAGUIRRE, LCALDAS, LGUTIERREZ |

**Why classified as AUTOMATIC:** 100% automatic. ZR is an automatically assigned receivables document type — cannot be manually created.

---

#### 34. FB70 — Enter Customer Credit Memo

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 72 (100.0%) |
| **Document types** | DR (Customer Invoice Clearing) |
| **Representative human users** | AOSORIO, FERUIZ |

**Why classified as AUTOMATIC:** 100% automatic. DR document type is system-assigned for customer invoice clearing.

---

#### 35. FBDC_C022 — Custom Utility Clearing

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 155 (100.0%) |
| **Document types** | DZ (Customer Payment Clearing), SU (Standard Utility) |
| **Representative human users** | AOSORIO, DPINILLA, FERUIZ |

**Why classified as AUTOMATIC:** 100% automatic. DZ and SU are standard clearing and utility document types.

---

#### 36. FBA7 — Automated Account Transactions

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 38 (100.0%) |
| **Document types** | KZ (Payment Clearing), SU (Standard Utility) |
| **Representative human users** | CALVAREZ, DCOSTO, JTOCANCHON, MOLIVEIRA |

**Why classified as AUTOMATIC:** 100% automatic. KZ and SU document types confirm automated clearing.

---

#### 37. ZMM_CARGA_MIRO_MX — Automated Batch Import (Mexico)

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 18 (100.0%) |
| **Document types** | AA (Automatic Accounting) |
| **Representative human users** | OSOSA |

**SAP Description:** ZMM_CARGA_MIRO_MX is a custom Nubank transaction for Mexico-specific automated batch invoice loading (MIRO batch import). All postings are system-generated AA documents.

**Why classified as AUTOMATIC:** 100% automatic. AA document type confirms system-generated entries. This is a batch import tool, not a discretionary posting screen.

---

#### 38. AS02 — Change Asset Master Record

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 4 (100.0%) |
| **Document types** | AA (Automatic Accounting) |
| **Representative human users** | DFERREIRA |

**Why classified as AUTOMATIC:** 100% automatic. Master data changes that trigger financial postings do so through system-determined accounting logic.

---

#### 39. AB01L — Create Asset Posting

| Attribute | Value |
|---|---|
| **Classification** | ✅ AUTOMATIC POSTING |
| **Automatic posting lines** | 6 (100.0%) |
| **Document types** | AA (Automatic Accounting) |
| **Representative human users** | RCASTILLO |

**Why classified as AUTOMATIC:** 100% automatic. Asset creation postings (AA) are system-determined from asset master data.

---

## Complete Classification Table — All 39 Transaction Codes

| # | Transaction Code | Classification | Total Lines | Manual Lines | Auto Lines | Manual % | Primary Document Types |
|---|---|---|---|---|---|---|---|
| 1 | FBDC_P001 | 🔴 MANUAL | 1,079,221 | 1,074,437 | 4,784 | 99.6% | SA, CP, FP, PR, RF, GO, TX, SR, FI, IC, BK, N1, VC |
| 2 | ZFI_ADP | 🔴 MANUAL | 380,618 | 380,618 | 0 | 100.0% | FP |
| 3 | FBD5 | 🔴 MANUAL | 572 | 572 | 0 | 100.0% | GO, SA |
| 4 | FB01 | ✅ AUTOMATIC | 2,568,096 | 0 | 2,568,096 | 0.0% | ZR, TI |
| 5 | KSV5 | ✅ AUTOMATIC | 976,500 | 0 | 976,500 | 0.0% | CO, CS |
| 6 | AFABN | ✅ AUTOMATIC | 449,724 | 0 | 449,724 | 0.0% | AF |
| 7 | FAGL_IT_02 | ✅ AUTOMATIC* | 1,227,912 | 5,468 | 1,222,444 | 0.4% | EC, N1 |
| 8 | F110 | ✅ AUTOMATIC | 195,049 | 0 | 195,049 | 0.0% | ZP, SU |
| 9 | FB08 | ✅ AUTOMATIC* | 317,082 | 3,788 | 313,294 | 1.2% | ES, FP, IC, N1 |
| 10 | FBB1 | ✅ AUTOMATIC* | 72,816 | 630 | 72,186 | 0.9% | SU, FI, SA, VC, YH |
| 11 | MIRO | ✅ AUTOMATIC | 93,676 | 2 | 93,674 | 0.0% | AA, KR, RE, SR |
| 12 | KO8G | ✅ AUTOMATIC | 44,918 | 0 | 44,918 | 0.0% | AA, ES |
| 13 | FBVB | ✅ AUTOMATIC | 19,190 | 0 | 19,190 | 0.0% | KR, KS |
| 14 | LSMW | ✅ AUTOMATIC | 16,496 | 0 | 16,496 | 0.0% | AA |
| 15 | FB05 | ✅ AUTOMATIC | 9,737 | 0 | 9,737 | 0.0% | KR, KZ, TI, ZR |
| 16 | F111 | ✅ AUTOMATIC | 7,414 | 0 | 7,414 | 0.0% | ZP, ZR, ZV |
| 17 | AB08 | ✅ AUTOMATIC | 5,335 | 0 | 5,335 | 0.0% | ES |
| 18 | FBDC_C014 | ✅ AUTOMATIC | 4,884 | 0 | 4,884 | 0.0% | KZ, ZP |
| 19 | ABUMN | ✅ AUTOMATIC | 3,660 | 0 | 3,660 | 0.0% | AA |
| 20 | FBZ2 | ✅ AUTOMATIC | 3,823 | 0 | 3,823 | 0.0% | KZ |
| 21 | FBDC_C002 | ✅ AUTOMATIC | 683 | 0 | 683 | 0.0% | SU |
| 22 | ABZON | ✅ AUTOMATIC | 1,214 | 0 | 1,214 | 0.0% | AA, AF |
| 23 | FB1K | ✅ AUTOMATIC | 1,513 | 0 | 1,513 | 0.0% | SU |
| 24 | FB1S | ✅ AUTOMATIC | 1,017 | 0 | 1,017 | 0.0% | SU |
| 25 | ABAVN | ✅ AUTOMATIC | 371 | 0 | 371 | 0.0% | AA |
| 26 | ZLIA_COCKPIT | ✅ AUTOMATIC | 406 | 0 | 406 | 0.0% | AA |
| 27 | FBDC_C024 | ✅ AUTOMATIC | 395 | 0 | 395 | 0.0% | KZ |
| 28 | MR8M | ✅ AUTOMATIC | 226 | 0 | 226 | 0.0% | AA, RE |
| 29 | KO88 | ✅ AUTOMATIC | 206 | 0 | 206 | 0.0% | AA, ES |
| 30 | MIR4 | ✅ AUTOMATIC | 140 | 0 | 140 | 0.0% | AA |
| 31 | FBL1N | ✅ AUTOMATIC | 103 | 0 | 103 | 0.0% | ES |
| 32 | FV60 | ✅ AUTOMATIC | 102 | 0 | 102 | 0.0% | KG |
| 33 | FBDC_C080 | ✅ AUTOMATIC | 82 | 0 | 82 | 0.0% | ZR |
| 34 | FB70 | ✅ AUTOMATIC | 72 | 0 | 72 | 0.0% | DR |
| 35 | FBDC_C022 | ✅ AUTOMATIC | 155 | 0 | 155 | 0.0% | DZ, SU |
| 36 | FBA7 | ✅ AUTOMATIC | 38 | 0 | 38 | 0.0% | KZ, SU |
| 37 | ZMM_CARGA_MIRO_MX | ✅ AUTOMATIC | 18 | 0 | 18 | 0.0% | AA |
| 38 | AS02 | ✅ AUTOMATIC | 4 | 0 | 4 | 0.0% | AA |
| 39 | AB01L | ✅ AUTOMATIC | 6 | 0 | 6 | 0.0% | AA |

*\* Codes marked with asterisk are predominantly automatic but contain a minor manual subset that should be included in the MJE population for SOX testing.*

---

## SOX MJE Population — Complete Extraction Criteria

To extract the complete MJE population from the source data for SOX testing purposes:

```sql
-- Primary MJE population (definitive)
SELECT *
FROM journal_entries
WHERE movement_type = 'manual'

-- This produces the following breakdown:
--   FBDC_P001:  1,074,437 lines  (73.3% of MJE population)
--   ZFI_ADP:      380,618 lines  (26.0% of MJE population)
--   FBD5:             572 lines   (0.0% of MJE population)
--   FAGL_IT_02:     5,468 lines   (0.4% of MJE population)
--   FB08:           3,788 lines   (0.3% of MJE population)
--   FBB1:             630 lines   (0.0% of MJE population)
--   MIRO:               2 lines   (0.0% of MJE population)
--   TOTAL:      1,465,515 lines  (100%)
```

---

## References

| Reference | Purpose |
|---|---|
| `New_Query_2026_02_25_16_33_43 (1).csv` | Primary source data (11,008,486 posting lines) |
| `FINAL_Classification_Criteria_Definition.md` | Classification criteria and definitions |
| `Manual_vs_Automatic_Journal_Entries.md` | Detailed comparison tables |
| `docs/memos/manual_journal_entries_vs_automatic_postings_memo.md` | Controllership memo |
| SAP Transaction SE16 / Table T003 | SAP document type master data |
| SAP Transaction SE16 / Table BKPF | SAP accounting document header |

---

*Document version: FINAL | Prepared: 2026-03-11 | Author: amandaocosta*
