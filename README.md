# InnovAIte 2026 — From Legacy to Leading Edge

## Microsoft Fabric Hands-On Lab

This repository contains all materials for the **Microsoft Fabric** session at InnovAIte 2026. The session walks attendees through building an end-to-end data analytics solution using Microsoft Fabric — from ingesting data out of a SQL database to delivering an interactive Power BI dashboard.

### Scenario

You are a data analyst at **InnovAItion Partners Ltd.**, a technology reseller. Your company sells hardware, software, cloud services, and networking equipment from vendors like Microsoft, Dell, HP, Cisco, and Fortinet. Leadership wants a unified view of the business — and you're going to build it with Microsoft Fabric.

---

## Repository Structure

```
├── Lab/
│   ├── LabGuide.md                          # Step-by-step hands-on lab guide
│   └── Setup MFA & Change Password.md       # First-time tenant login instructions
│
├── Generator/
│   ├── generate_sql.py                      # Python script to generate fake data
│   └── InnovAItion_Partners_Lab.sql         # SQL seed script for Azure SQL Database
│
├── SEAMAN - From Legacy to Leading Edge.pptx  # Slide deck
└── README.md                                  # You are here
```

| Directory / File | Purpose |
|---|---|
| **Lab/** | Everything attendees need during the hands-on portion |
| **Lab/LabGuide.md** | The main lab guide — start here for the hands-on lab |
| **Lab/Setup MFA & Change Password.md** | Instructions for setting up MFA and changing your password on first login |
| **Generator/** | Scripts used to generate and seed the lab database (instructor use only) |
| **Generator/generate_sql.py** | Python script that generates 50 customers and 1,000 sales orders |
| **Generator/InnovAItion_Partners_Lab.sql** | The generated SQL script — run this against Azure SQL to populate the lab database |

---

## Session Agenda

| Section | Duration | Description |
|---|---|---|
| Slides | 30-45 min | From Legacy to Leading Edge — why Fabric matters for resellers |
| Lab 1 | 10-15 min | Environment setup — Fabric trial, workspace, Lakehouse |
| Lab 2 | 15-20 min | Ingest Sales Orders via Data Pipeline |
| Lab 3 | 10-15 min | Ingest Customers via Dataflow Gen2 |
| Lab 4 | 20-25 min | Transform & model — relationships, DAX measures |
| Lab 5 | 15-20 min | Build a Power BI dashboard |
| Q&A | 20 min | Questions and discussion |

---

## Getting Started

1. **First-time login?** Follow the [MFA & Password Setup Guide](Lab/Setup%20MFA%20%26%20Change%20Password.md)
2. **Ready for the lab?** Open the [Lab Guide](Lab/LabGuide.md) and start at Lab 1

---

## Prerequisites

- A modern web browser (Edge or Chrome recommended) — **use InPrivate / Incognito mode**
- Credentials provided by the instructor
- Azure SQL connection details (provided in the lab guide)
