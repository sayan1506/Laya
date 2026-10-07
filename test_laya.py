from laya import Router

router = Router(preload=True)  # loads checkpoints upfront, avoids reload latency later

state = {"body": "Hi, we were billed twice for March. Please refund today or we'll cancel."}

questions = {
    "department": {
        "type": "choice",
        "instructions": "Which department should handle this?",
        "criteria": {"billing": "invoices, refunds", "technical": "bugs, outages", "other": "everything else"}
    },
    "urgency": {"type": "score", "instructions": "How urgent is this?", "criteria": ["not urgent", "soon", "critical"]},
    "churn_risk": {"type": "noul", "instructions": "Does the user threaten to cancel?"}
}

res = router.predict(state, questions)
print(res["answers"]["department"]["choice"])   # -> billing
print(res["answers"]["urgency"]["score"])
print(res["answers"]["churn_risk"]["noul"])      # probability from 0 to 1