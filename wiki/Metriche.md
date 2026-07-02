---
title: Metriche
tags:
  - osint
  - sna
  - network-analysis
status: NEW_HEALED
tipo: sintesi
depth: standard
date: "2026-05-16"

---

# Metriche nella Social Network Analysis per OSINT

La Social Network Analysis (SNA) applicata all'OSINT si avvale di fondamenti matematici rigorosi (Teoria dei Grafi) per identificare pattern strutturali, comunità e hub di disinformazione. L'efficacia della SNA non si basa solo sulla mappatura visiva (es. Gephi), ma sul calcolo di **metriche di centralità** che quantificano il ruolo strategico di ciascun nodo (utente, entità, dominio) all'interno dell'infrastruttura di rete.

### Metriche Centrali

- **Degree Centrality**: Misura la "popolarità" o il numero di connessioni dirette di un nodo. In OSINT, identifica l'utente più prolifico o il dominio più linkato.
- **Betweenness Centrality**: Quantifica quante volte un nodo funge da "ponte" lungo i percorsi più brevi tra altri nodi. È cruciale in intelligence perché identifica i *broker informativi*, ovvero i nodi che controllano il flusso di informazioni tra comunità o bolle isolate (echo chambers). Un nodo con alta betweenness può manipolare o interrompere un network.
- **Closeness Centrality**: Misura la distanza media di un nodo da tutti gli altri. Identifica chi può diffondere informazioni all'intera rete nel minor tempo possibile.
- **Eigenvector Centrality**: Pesata sull'importanza dei vicini (simile all'algoritmo [[PageRank]]). Un nodo è importante se è connesso ad altri nodi importanti.

### Implicazioni OSINT

L'analisi empirica (es. su dataset come *Storm of Swords*) dimostra empiricamente la distinzione tra Degree (nodo pop) e Betweenness (nodo broker). Nell'OSINT contemporaneo, la SNA si focalizza sul "behavior-based approach", rilevando pattern strutturali automatizzati (botnet, coordinated sharing) indipendentemente dal contenuto semantico dei messaggi, sebbene richieda sempre la validazione dell'intenzionalità da parte dell'analista.

## 🔗 Connessioni e Pattern

- [[Reti sociali]]
- [[Reti bipartite]]
- [[Disinformazione]]
- [[Trattamento dell'output]]
- [[Dashboarding con ai]]

- [[-- F/I/H ---]]
- [[**Fatti (F)**: Le metriche di centralità (Degree, Betweenness, Closeness, Eigenvector) permettono di qualificare oggettivamente il ruolo di un nodo in una rete.]]
- [[**Interpretazione (I)**: In ottica OSINT/Counter-Disinformation, i nodi con alta Betweenness sono bersagli strategici primari perché diSATtivarli o monitorarli frammenta l'efficienza della diffusione di una campagna avversaria.]]
- [[**Ipotesi (H)**: Nelle campagne ibride future, gli attori malevoli impiegheranno AI per nascondere i propri "broker" (riducendo artificialmente la loro Betweenness visibile) distribuendo il coordinamento su reti bipartite decentralizzate e frammentate.]]
