class ServicioPagos:
    def __init__(self, api_key: str = "mock_key", provider: str = "mercadopago"):
        self.api_key = api_key
        self.provider = provider

    def procesar_pago(self, pedido, token_tarjeta: str) -> dict:
        print(f"Procesando pago para pedido {pedido.id_pedido} por ${pedido.monto}")
        print(f"Proveedor: {self.provider}, Token: {token_tarjeta[:10]}...")
        return {
            "status": "success",
            "transaction_id": f"txn_{pedido.id_pedido}_mock",
            "message": "Pago procesado correctamente"
        }