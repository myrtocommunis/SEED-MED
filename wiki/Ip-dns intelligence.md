---
title: "Ip-dns intelligence"
tags: ["OSINT", "processed", "cyber", "dns", "infrastruttura"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Ip-dns intelligence

## 🎯 Sintesi Strategica

L'**IP/DNS Intelligence** è il processo investigativo di disvelamento dell'infrastruttura di rete celata dietro un nome a dominio (website). Nell'[[Osint]], questa disciplina scavalca l'anonimato del web: se l'amministratore di un sito di [[Disinformazione]] usa dati falsi per registrare un dominio (WHOIS Privacy), l'analista indaga i record DNS e gli IP storici per svelare server condivisi, indirizzi fisici e altri siti malevoli connessi al medesimo host.

## 📚 Contesto e Definizioni

I Domain Name System (DNS) sono la rubrica telefonica di Internet. L'indagine si concentra sui Record:
*   **Record A / AAAA:** L'indirizzo IP (IPv4 o IPv6) del server.
*   **Record MX (Mail Exchange):** Rivela quale provider gestisce le email del target (es. Google Workspace o un server russo privato).
*   **Record TXT:** Spesso contiene chiavi di verifica (SPF, DMARC) utilizzate dai ricercatori per dimostrare che due domini apparentemente scorrelati sono gestiti dalla stessa persona.

## 📊 Dati, Tecnologie e Metriche

L'arma assoluta di questa disciplina è il **[[Passive DNS]] (pDNS)**. Strumenti come Securitytrails o DNSDumpster registrano storicamente le modifiche ai record. Se un Threat Actor oggi nasconde il sito dietro Cloudflare (mascherando l'IP), il pDNS permette di "tornare indietro nel tempo" e visualizzare l'IP reale (Origin IP) che il sito aveva prima di attivare la protezione.

## 🔗 Connessioni e Pattern

- [[Network intelligence]]
- [[Cyber]]
- [[Opsec]]
- [[--]]
F/I/H
- [[--]]
