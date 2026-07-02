# Release Policy — Quality Gate

Nessun agente passa a `stable` senza:
1. **Smoke test passato** (vedi `system/50_evals/smoke_tests/`).
2. **Rubrica soddisfatta** (vedi `system/50_evals/rubrics/`).
3. **Approvazione umana esplicita.**

## Stato agenti
| Agente | Smoke test | Stato |
|--------|-----------|-------|
| architect | pending | draft |
| curator | pending | draft |
| adversary | pending | draft |
| reporter | pending | draft |

La promozione delle NOTE (`draft → validated`) è sempre e solo umana.
