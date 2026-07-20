param(
    [Parameter(Mandatory = $true)]
    [string]$EvidenceId,

    [Parameter(Mandatory = $true, ValueFromRemainingArguments = $true)]
    [string[]]$Command
)

$ErrorActionPreference = "Stop"
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$logDir = Join-Path $repoRoot "reports/logs/week_1"
New-Item -ItemType Directory -Force $logDir | Out-Null
$logPath = Join-Path $logDir "$EvidenceId.txt"
$start = [DateTimeOffset]::UtcNow

$header = @(
    "evidence_id=$EvidenceId",
    "started_at_utc=$($start.ToString('o'))",
    "repository_root=$repoRoot",
    "command=$($Command -join ' ')"
)
$header | Set-Content -Path $logPath -Encoding utf8

& $Command[0] $Command[1..($Command.Count - 1)] 2>&1 |
    Tee-Object -FilePath $logPath -Append
$childExitCode = $LASTEXITCODE

$finish = [DateTimeOffset]::UtcNow
@(
    "finished_at_utc=$($finish.ToString('o'))",
    "exit_code=$childExitCode"
) | Add-Content -Path $logPath -Encoding utf8

$hash = (Get-FileHash -Algorithm SHA256 -Path $logPath).Hash.ToLowerInvariant()
Write-Output "log_path=$logPath"
Write-Output "sha256=$hash"
exit $childExitCode
