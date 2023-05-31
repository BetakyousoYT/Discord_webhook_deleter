import requests

def delete_webhook(webhook_url):
    response = requests.delete(webhook_url)
    if response.status_code == 204:
        print("Webhookを削除しました。")
    else:
        print("Webhookの削除に失敗しました。")

webhook_url = input("WebhookのURLを入力してください: ")
delete_webhook(webhook_url)
