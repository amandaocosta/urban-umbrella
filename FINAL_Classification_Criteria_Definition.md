# FINAL Classification Criteria Definition
## Manual Journal Entries vs. Automatic Postings — Nubank Financial Accounting

**Document Status:** FINAL — Approved for Distribution  
**Prepared by:** Amanda O. Costa  
**Date:** 2026-03-11  
**Distribution:** Controllership Director | SOX Team  
**Source Data:** New_Query_2026_02_25_16_33_43 (1).csv — 11,008,486 total posting lines analyzed

---

## 1. Executive Summary

### Single, Clear Definition

> **A posting is classified as a Manual Journal Entry if the `movement_type` field in the source system equals `"manual"`, which is driven by three independently observable factors: (1) the transaction code is purpose-built for discretionary human posting, (2) the entry is created under an individual named user's identity rather than a system/batch account, and (3) the entry requires human judgment, approval, and individual accountability before it is committed to the General Ledger.**
>
> **All other postings — where `movement_type` equals `"automatic"` — are classified as Automatic Postings and do not require a manual approval gate.**

**Population summary from production data:**

| Classification | Total Posting Lines | Share of Total |
|---|---|---|
| Automatic Postings | 9,542,971 | **86.7%** |
| Manual Journal Entries | 1,465,515 | **13.3%** |
| **Grand Total** | **11,008,486** | **100%** |

---

## 2. Classification Criteria — The 3 Core Factors

The classification of a posting as Manual or Automatic is determined by three mutually reinforcing factors. All three factors converge on the same conclusion in the production data.

### Factor 1 — Source System `movement_type` Field (Primary Criterion)

The SAP source data contains an explicit `movement_type` column populated at the time of posting. This is the **definitive, authoritative criterion**.

| `movement_type` Value | Classification | SOX Implication |
|---|---|---|
| `manual` | **Manual Journal Entry** — requires approval | Subject to MJE controls |
| `automatic` | **Automatic Posting** — no approval gate required | Outside MJE control scope |

*This field is system-assigned based on the transaction code and posting path used. It cannot be changed by the end user at the time of entry.*

---

### Factor 2 — Transaction Code Design (Corroborating Criterion)

The SAP transaction code used to create the entry indicates whether the posting path was designed for discretionary human input or for rule-driven automated processing.

**Transaction codes classified as Manual (by data evidence):**

| Transaction Code | SAP Description | Manual Lines | Manual % | Key Users |
|---|---|---|---|---|
| **FBDC_P001** | Manual Posting Module — Primary GL Entry Screen | 1,074,437 | 99.6% | Individual named accountants |
| **ZFI_ADP** | Manual Financial Adjustments (ADP Integration) | 380,618 | 100.0% | HBALBINO, JEPEREIRA |
| **FBD5** | Manual Reversal / Recurring Entry Posting | 572 | 100.0% | CALCANTARA, ISOUZA, MREIS |

**All remaining 36 transaction codes** produce exclusively or overwhelmingly automatic postings (see Section 3 and the full analysis in `Analysis_All_39_Transaction_Codes.md`).

---

### Factor 3 — Creator User Identity (Corroborating Criterion)

The `creator_user_id` field records who initiated the posting. Individual named users posting through manual transaction codes carry personal accountability; system/batch accounts execute automated processes.

**System/Batch Accounts (Automatic Posting owners):**

| Account ID | System / Process | Role |
|---|---|---|
| `LAMBDA_PNU_P` | AWS Lambda automated process | Batch GL postings — highest volume system account |
| `SAPCPI` | SAP Cloud Platform Integration | Core system integration processes and clearing |
| `USERJOB` | SAP Scheduled Batch Jobs | Payment runs, invoice batches, recurring entries |
| `SAP_WFRT` | SAP Workflow Runtime | Workflow-triggered automatic postings |
| `CASHMGTBR` | Cash Management System (Brazil) | Automatic cash position postings |

**Individual Named Users (Manual Journal Entry owners):**  
162 distinct human users appear in the dataset. Users posting through FBDC_P001, ZFI_ADP, or FBD5 are making manual journal entries requiring approval (e.g., DFERREIRA, HBALBINO, FSOUZA, JEPEREIRA, SBORECKI, JEPEREIRA, NCAMACHO, PSAMPAIO).

---

## 3. Definitions

### Manual Journal Entry — Final Definition

> A **Manual Journal Entry (MJE)** is any financial posting created through a transaction code designed for discretionary human input (FBDC_P001, ZFI_ADP, or FBD5), executed under an individual named user's identity, that is recorded with `movement_type = "manual"` in the source system. Manual journal entries represent human judgment applied to the accounting record and are **subject to the full SOX MJE control framework**: preparation, independent review, managerial approval, and documented business justification prior to posting.

**Key attributes:**
- `movement_type` = `"manual"`
- Transaction code: FBDC_P001, ZFI_ADP, or FBD5
- `creator_user_id` = individual named person (not a system/batch account)
- Requires segregation of duties (preparer ≠ approver)
- Requires supporting documentation and business justification
- Subject to period-end completeness review

---

### Automatic Posting — Final Definition

> An **Automatic Posting** is any financial posting generated by the SAP system or an integrated automated process, executing pre-configured accounting rules without discretionary human input at the moment of posting, recorded with `movement_type = "automatic"` in the source system. Automatic postings are **outside the scope of the MJE approval control** but remain subject to IT General Controls (ITGCs) and configuration change management controls.

**Key attributes:**
- `movement_type` = `"automatic"`
- Transaction code: any of the 36 automated transaction codes (F110, FB01, MIRO, KSV5, AFABN, etc.)
- `creator_user_id` may be a system account or a human user initiating a workflow that fires automated rules
- No individual approval gate at the time of posting
- Governed by configuration change management and ITGCs
- Monitored through automated reconciliation and exception reporting

---

## 4. Decision Tree

```
START: Evaluate a posting line
           │
           ▼
┌─────────────────────────────────────────┐
│ What is the movement_type field value?  │
└─────────────────────────────────────────┘
           │
    ┌──────┴──────┐
    │             │
"manual"     "automatic"
    │             │
    ▼             ▼
┌─────────┐  ┌──────────────────────────┐
│ Confirm │  │  AUTOMATIC POSTING       │
│ txn     │  │  → No approval required  │
│ code is │  │  → IT/config controls    │
│ FBDC_   │  │    apply                 │
│ P001,   │  └──────────────────────────┘
│ ZFI_ADP,│
│ or FBD5 │
└────┬────┘
     │
   YES
     │
     ▼
┌────────────────────────────────────────┐
│  MANUAL JOURNAL ENTRY                  │
│  → Preparation by named individual     │
│  → Independent review required         │
│  → Managerial approval required        │
│  → Business justification documented   │
│  → Segregation of duties applied       │
│  → Retained per records policy         │
└────────────────────────────────────────┘
```

---

## 5. Quick Reference Table

| Criterion | Manual Journal Entry | Automatic Posting |
|---|---|---|
| **`movement_type`** | `manual` | `automatic` |
| **Transaction codes** | FBDC_P001, ZFI_ADP, FBD5 | All other 36 codes (F110, FB01, MIRO, KSV5, etc.) |
| **Creator user** | Individual named person | System account OR human initiating automated rule |
| **Approval required?** | 🔴 **YES — mandatory before posting** | ✅ No — system validates automatically |
| **Supporting docs** | Required (business justification, backup) | Not required for individual entries |
| **Segregation of duties** | Required (preparer ≠ approver) | Not applicable |
| **SOX MJE control** | **In scope** | Out of scope (ITGCs apply) |
| **Audit trail** | Individual accountability tracked | System-generated automatically |
| **Typical volume** | 13.3% of total posting lines | 86.7% of total posting lines |
| **Document types used** | SA, CP, FP, PR, RF, GO, TX, SR, FI, IC, BK, N1, VC, CR, CS, BK, ZR, YX | AA, AF, ES, ZP, ZR, YX, YN, YB, YI, YC, YA, YL, YD, YM, YP, KR, KS, KZ, EC, TI, DR, CC, HR, DZ, SU, KG, RE, CO, CS, SC, TX |

---

## 6. Implementation Checklist

### For the SOX / Internal Controls Team

- [ ] **MJE population definition:** Use `movement_type = "manual"` as the primary filter to extract the MJE population for testing
- [ ] **Completeness assertion:** Validate that all postings through FBDC_P001, ZFI_ADP, and FBD5 are captured in the MJE population (cross-check transaction codes)
- [ ] **User access review:** Confirm that access to FBDC_P001 and ZFI_ADP is restricted to authorized accounting personnel; no system/batch accounts should have posting rights through these codes
- [ ] **Approval evidence:** For each sampled MJE, obtain approval documentation (electronic sign-off, workflow record, or email approval with business justification)
- [ ] **Segregation of duties:** Verify preparer ≠ approver for all sampled entries; flag any self-approved postings
- [ ] **Completeness and cut-off:** Confirm that no manual postings were made after the period-end close without proper back-posting approval
- [ ] **Automated posting configuration:** Separately confirm that configuration changes to automated rules (for the 36 automatic transaction codes) are subject to ITGC change management controls
- [ ] **Monitoring control:** Verify that a detective control exists to identify any `movement_type = "automatic"` postings made through manual transaction codes (exception = potential control gap)

### For the Controllership / Finance Operations Team

- [ ] **Training:** Ensure all accountants with access to FBDC_P001, ZFI_ADP, and FBD5 understand that these transactions produce MJEs requiring approval
- [ ] **Approval workflow:** Confirm the SAP approval workflow is active and enforced for all postings through the three manual transaction codes
- [ ] **Period-end close checklist:** Include MJE review as a mandatory step in the period-end close checklist
- [ ] **Exception reporting:** Implement a weekly/monthly report of all MJEs by user, document type, and amount for management review
- [ ] **Threshold-based escalation:** Define amount thresholds that escalate MJE approval to senior management or CFO
- [ ] **Recurring entry review:** FBD5 (recurring entry posting) entries should be reviewed at each period-end to confirm continued business relevance

---

## 7. References

| Reference | Purpose |
|---|---|
| `New_Query_2026_02_25_16_33_43 (1).csv` | Primary source data — 11,008,486 posting lines |
| `Manual_vs_Automatic_Journal_Entries.md` | Detailed comparison tables and workflow documentation |
| `Analysis_All_39_Transaction_Codes.md` | Full analysis of all 39 named transaction codes |
| `docs/memos/manual_journal_entries_vs_automatic_postings_memo.md` | Memo to Controllership Director and SOX Team |
| SAP Table T003 | Document type master data |
| SAP Table BKPF | Accounting document header |

---

*Document version: FINAL | Prepared: 2026-03-11 | Author: amandaocosta*
