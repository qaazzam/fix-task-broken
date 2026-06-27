Parse the Apache-style access log at `/app/access.log` and produce a JSON summary report.

Write the report to `/app/report.json` with the following structure:

```json
{
  "total_requests": <int>,
  "unique_ips": <int>,
  "top_path": "<string>"
}
```

Success criteria:

1. The file `/app/report.json` exists and is valid JSON.
2. `total_requests` is the total number of log lines (requests).
3. `unique_ips` is the count of distinct client IP addresses.
4. `top_path` is the request path (e.g. `/index.html`) that appears most often.
