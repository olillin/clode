Function clode {
    param(
        [string]$id,
        [string]$output = $null  # Make $output optional
    )

    # Resolve short-id
    if ($id -match "^[a-zA-Z0-9._-]+$") {
        # Attempt to use default username
        if (-not $env:DEFAULT_CLODE_USERNAME) {
            Write-Output "No username provided and %DEFAULT_CLODE_USERNAME% is unset"
            return $null
        }

        $id = $env:DEFAULT_CLODE_USERNAME + "/" + $id
    }

    if ($id -match "^[a-zA-Z0-9._-]+/[a-zA-Z0-9._-]+$") {
        $id = "https://github.com/" + $id
        Write-Output "Resolved id to '$id'"
    }


    # Clone the Git repo
    $gitCloneResult = Start-Process git -NoNewWindow -ArgumentList "clone $id $output" -Wait -PassThru

    # Exit if failure
    if ($gitCloneResult.ExitCode -ne 0) {
        Write-Output "git clone failed"
        return $null
    }

    # Extract the directory path from the output
    $outputFolder = $output
    if (-not $output) {
        $outputFolder = ($id -replace "\.git$", "" | Select-String -Pattern "(?<=/)[a-zA-Z0-9._-]+(?!.*/)").Matches[0].value
    }

    Write-Output "Opening '$outputFolder' in VSCode..."

    # Open the output folder with code
    code $outputFolder
}