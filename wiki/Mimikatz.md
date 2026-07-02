---
title: "Mimikatz"
tags: ["OSINT", "processed", "mimikatz", "cyber", "credenziali", "windows"]
date: "2026-05-15"
status: "draft"
depth: "standard"
sources: "2"
tipo: "concetto"
---

# Mimikatz

## 🎯 Sintesi Strategica

**Mimikatz** è uno strumento di sicurezza open-source estremamente potente (creato come Proof of Concept) divenuto l'arma d'elezione sia per i Penetration Tester che per i peggiori attori di minaccia globali (Ransomware gang e gruppi [[Apt]]). La sua funzione principale è l'estrazione in chiaro di password, codici PIN e token (Kerberos Tickets) dalla memoria RAM dei sistemi operativi Windows (processo LSASS). È il pilastro tecnico della fase di "Privilege Escalation" in un attacco informatico.

## 📚 Contesto e Definizioni

In una tipica [[Cyber kill chain]], dopo aver violato l'account di un dipendente base tramite [[Attacco di phishing]] (Lateral Movement), l'hacker non ha i permessi per distruggere l'intera rete. L'attaccante esegue Mimikatz sul PC compromesso. Se in passato un amministratore di rete (Domain Admin) ha effettuato il login su quel PC per fare manutenzione, Mimikatz recupera la password dell'amministratore rimasta memorizzata in RAM, garantendo all'hacker il controllo totale e istantaneo dell'intera infrastruttura aziendale.

## 📊 Dati, Tecnologie e Metriche

Tra le sue tecniche più letali vi sono il "Pass-the-Hash" (riutilizzare l'hash crittografico della password senza doverla decifrare) e il "Golden Ticket" (la forgiatura di un token di autenticazione illimitato che inganna i server Microsoft). Monitorare l'uso di Mimikatz è la priorità assoluta per i Security Operation Center (SOC); i difensori implementano policy di hardening severe (come disabilitare WDigest) per rendere la memoria RAM inaccessibile ai dump di estrazione.

## 🔗 Connessioni e Pattern

- [[Cyber kill chain]]
- [[Apt]]
- [[Cybersecurity]]
- [[--]]
F/I/H
- [[--]]
