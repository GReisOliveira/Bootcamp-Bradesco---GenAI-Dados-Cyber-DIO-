#Pegar o diretório atual
$scriptDirectory = Split-Path $Myinvocation.MyCommand.Definition -Parent

#Arquivo saida com todos sql
$outputFile = Join-Path -Path $scriptDirectory -ChildPath "migration.sql"

#Verificar se arquivo ja existe, se existir deleta
if (Test-Path $outputFile) {
    Remove-Item $outputFile
}

#Pega Conteúdo dos arquivos
$sqlFiles = Get-ChildItem -Path $scriptDirectory -Filter *.sql | Sort-Object Name

#Concatena Arquivos
foreach($file in $sqlFiles) {
    Get-content $file.FullName | Out-File -Append -FilePath $outputFile
    "GO" | Out-File -Append -FilePath $outputFile
}

Write-Host "Todos os arquivos SQL foram combinados em $outputFile"