$folderNames = @(
    "Openbanking.AltaUsuario",
    "api-cuenta-extracto",
    "api-openbanking-cobro-comision",
    "OpenBanking.ConsultarCuentas",
    "pago-proveedores-transferencia-interbancaria-anular",
    "pago-proveedores-transferencia-interbancaria-aprobar",
    "pago-proveedores-transferencia-interbancaria-consultar",
    "pago-proveedores-transferencia-interbancaria-crear",
    "pago-proveedores-transferencia-interna-crear",
    "pago-proveedores-transferencia-interna-consultar",
    "pago-proveedores-transferencia-interna-aprobar",
    "pago-proveedores-transferencia-interna-anular"
)

$baseDirectory = "C:/Users/alvaro.Rodriguez/Desktop/Quality_Assurance_24/JULIO_24/UH - 180652 - Willian Paez/test cases"  # Or the desired base directory

for ($i = 0; $i -lt $folderNames.Count; $i++) {
    $folderName = "CP {0:D2} - {1}" -f ($i + 1), $folderNames[$i]
    $fullPath = Join-Path $baseDirectory $folderName
    New-Item -ItemType Directory -Path $fullPath
}
