# Mailman

A Django microservice for sending emails, SMS, WhatsApp, and push notifications via REST APIs.

## Quickstart

1. Clone this repository
2. Install requirements: `pip install -r requirements.txt`
3. Configure `.env` with your API keys/provider credentials
4. Run migrations: `python manage.py migrate`
5. Start the service: `python manage.py runserver`
6. Use the API endpoints as documented below

...

## API Usage Example

POST /api/send_email/

```
{
"to": "recipient@example.com",
"subject": "Welcome!",
"template": "welcome",
"params": {"name": "Recipient"}
}
```


...

## Contributing

Pull requests and suggestions welcome!
