# RenameFiles.ps1
# This script will:
# 1) Recursively look for all files in the specified folder (and sub-folders),
# 2) If a file’s name contains an underscore (_), rename the file replacing
#    the underscores with hyphens (-).

# Specify the path you want to scan
$TargetPath = 'C:\Users\maxah\Desktop\Graphics\Personal_Graphics\Hytopia_Design\Client_Assets\client_assets'

# Get all files recursively
Get-ChildItem -Path $TargetPath -Recurse -File | ForEach-Object {
    $originalName = $_.Name
    $newName = $originalName -replace '_', '-'

    # Only rename if there's a change
    if ($originalName -ne $newName) {
        try {
            Rename-Item -Path $_.FullName -NewName $newName
            Write-Host "Renamed '$originalName' to '$newName'"
        }
        catch {
            Write-Host "ERROR: Failed to rename '$originalName': $_"
        }
    }
}
