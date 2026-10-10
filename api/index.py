from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import numpy as np
import json

app = FastAPI()

# Enable CORS for POST from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.options("/api/latency")
async def options_handler():
    return Response(status_code=200)

TELEMETRY_DATA = json.loads("""
[
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 145.05,
    "uptime_pct": 99.343,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 232.72,
    "uptime_pct": 99.335,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 215.75,
    "uptime_pct": 99.494,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 112.75,
    "uptime_pct": 97.722,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 154.68,
    "uptime_pct": 98.998,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 217.45,
    "uptime_pct": 98.155,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 232.28,
    "uptime_pct": 98.203,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 161.33,
    "uptime_pct": 98.815,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 116.34,
    "uptime_pct": 99.429,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 156.61,
    "uptime_pct": 97.803,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 127.91,
    "uptime_pct": 98.507,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 188.54,
    "uptime_pct": 97.893,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 136.46,
    "uptime_pct": 97.745,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 131.97,
    "uptime_pct": 97.166,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 169.57,
    "uptime_pct": 98.962,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 145.29,
    "uptime_pct": 97.131,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 162.54,
    "uptime_pct": 99.138,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 200.73,
    "uptime_pct": 97.838,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 196.23,
    "uptime_pct": 98.019,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 228.53,
    "uptime_pct": 99.126,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 212.02,
    "uptime_pct": 97.706,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 122.61,
    "uptime_pct": 97.531,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 217.13,
    "uptime_pct": 98.733,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 178.12,
    "uptime_pct": 98.409,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 131.46,
    "uptime_pct": 98.68,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 130.59,
    "uptime_pct": 99.117,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 187.64,
    "uptime_pct": 98.431,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 208.26,
    "uptime_pct": 97.406,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 174.66,
    "uptime_pct": 98.139,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 212.28,
    "uptime_pct": 98.612,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 183.17,
    "uptime_pct": 97.89,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 154.5,
    "uptime_pct": 98.748,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 122.23,
    "uptime_pct": 98.579,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 144.52,
    "uptime_pct": 98.505,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 143.8,
    "uptime_pct": 97.329,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 171.73,
    "uptime_pct": 97.557,
    "timestamp": 20250312
  }
]
""")

@app.post("/api/latency")
async def latency_analytics(request: Request):
    body = await request.json()
    regions = body.get("regions", [])
    threshold_ms = body.get("threshold_ms", 180)

    results = []
    for region in regions:
        records   = [r for r in TELEMETRY_DATA if r["region"] == region]
        latencies = [r["latency_ms"] for r in records]
        uptimes   = [r["uptime_pct"]  for r in records]
        results.append({
            "region":      region,
            "avg_latency": round(float(np.mean(latencies)), 2),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime":  round(float(np.mean(uptimes)), 3),
            "breaches":    int(sum(1 for l in latencies if l > threshold_ms))
        })

    return {"regions": results}
