from src.sms.processors.first_bank import first_bank_processor
from src.sms.processors.access_bank import access_bank_processor
from src.sms.processors.gtbank import gtbank_processor
from src.sms.processors.keystone_bank import keystone_bank_processor
from src.sms.processors.uba import uba_processor
from src.sms.processors.wema_bank import wema_bank_processor
from src.sms.processors.zenith_bank import zenith_bank_processor

bank_processors = {
    "firstbank": first_bank_processor,
    "accessbank": access_bank_processor,
    "gtbank": gtbank_processor,
    "keystone": keystone_bank_processor,
    "uba": uba_processor,
    "wemabank": wema_bank_processor,
    "zenithbank": zenith_bank_processor,
}
