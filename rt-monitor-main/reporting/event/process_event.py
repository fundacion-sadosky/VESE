# Copyright (c) 2024 Fundacion Sadosky, info@fundacionsadosky.org.ar
# Copyright (c) 2024 INVAP, open@invap.com.ar
# SPDX-License-Identifier: AGPL-3.0-or-later OR Fundacion-Sadosky-Commercial

from reporting.event.event import Event


class ProcessEvent(Event):
    def __init__(self, time) -> None:
        super().__init__(time)

    @staticmethod
    def event_type():
        return "process_event"

    @staticmethod
    def decode_with(decoder, encoded_event):
        return decoder.decode_process_event(encoded_event)
