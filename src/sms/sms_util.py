from src.sms.processors import bank_processors


def process_bank_sms(data):
    """Processes bank sms"""
    message: str = data.get('message')
    sender: str = data.get('sender')
    uid = data.get('uid')
    date = data.get('createdAt')
    processor = bank_processors.get(sender.lower())
    if not processor:
        return None
    try:
        data = processor(message)
        return {**data, 'uid': uid, 'sender': sender, 'date': date}
    except Exception as e:
        return None


def remove_comma_from_number(number: str):
    """Returns a float of a string number"""
    return float(number.replace(',', ''))


def correct_balance_and_amount(data):
    """Corrects balance and amount"""
    amount = data.get('amount') or None
    balance = data.get('balance') or None
    if amount:
        amount = remove_comma_from_number(amount)
    if balance:
        balance = remove_comma_from_number(balance)
    return {**data, 'amount': amount, 'balance': balance}


def parse_data_for_worker_service(data):
    """Parses data for worker service"""
    return {
        'uid': data.get('uid'),
        'date': data.get('date'),
        'amount': data.get('amount'),
        'balance': data.get('balance'),
        'type': data.get('transaction_type'),
        'narration': data.get('description'),
        'sender': data.get('sender'),
    }
