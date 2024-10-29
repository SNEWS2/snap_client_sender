import asyncio
import datetime
from snews_pt.messages import Publisher, SNEWSHeartbeatMessage, \
                              SNEWSCoincidenceTierMessage,\
                              SNEWSRetractionMessage

#source from async generator
async def gen_timestamp(delay_seconds=1):
    """generate current timestamps with given delay"""
    while True:
        yield datetime.datetime.now()-datetime.timedelta(seconds=delay_seconds)

async def generate_heartbeat_message(detector_name=None):
    while True:
        yield SNEWSHeartbeatMessage(detector_name=detector_name,
                                    detector_status='ON')

def publish_to_snews(firedrill_mode=False, verbose=False):
    async def _send(source):
        with Publisher(firedrill_mode=firedrill_mode, auth=True, verbose=verbose) as pub:
            async for msg in source:
                yield pub.send([msg.message_data])
    return _send
                

def generate_coincidence_message(detector_name=None):
    def process(nu_time):
        return SNEWSCoincidenceTierMessage(detector_name=None, neutrino_time=nu_time)
    return process

        

def parse_alert_lines(max_delay=10):
    max_delay = datetime.timedelta(seconds=max_delay)
    async def _parse(source):
        async for line in source:
            if line.startswith('#'):
                continue
            observation_time = datetime.datetime.fromisoformat(line)
            dt = datetime.datetime.now()-observation_time
            if dt<max_delay:
                yield observation_time
    return _parse
    
