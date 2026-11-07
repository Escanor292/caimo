Add-Type -AssemblyName System.IO.Compression.FileSystem

$docxPath = "d:\AI-20261107T093517Z-1-001\AI\Master_Prompt_DT69_Full_GitHub_Tools.md.docx"
$zip = [System.IO.Compression.ZipFile]::OpenRead($docxPath)
$entry = $zip.Entries | Where-Object { $_.FullName -eq 'word/document.xml' }

if ($entry) {
    $stream = $entry.Open()
    $reader = New-Object System.IO.StreamReader($stream)
    $content = $reader.ReadToEnd()
    $reader.Close()
    $stream.Close()
    
    # Extract text from XML
    $content -replace '<[^>]+>', '' | Out-File -FilePath "d:\AI-20261107T093517Z-1-001\AI\extracted_text.txt" -Encoding UTF8
    Write-Host "Text extracted successfully"
} else {
    Write-Host "document.xml not found"
}

$zip.Dispose()
