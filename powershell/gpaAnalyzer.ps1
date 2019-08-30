[void][System.Reflection.Assembly]::LoadWithPartialName("System.windows.forms")    
$dialog = New-Object System.Windows.Forms.OpenFileDialog
$dialog.Filter = "単位修得状況確認表(*.html)|*.html"
$dialog.InitialDirectory = "~/Downloads"
$dialog.Title = "Choose the html file"

if($dialog.ShowDialog() -eq [System.Windows.Forms.DialogResult]::OK){
  ./python-3.6.8-embed-amd64/python ./src/gpaAnalyzer.py $dialog.FileName
}
