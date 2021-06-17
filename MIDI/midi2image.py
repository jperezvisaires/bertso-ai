import os

from music21 import converter, instrument, note, chord
import numpy as np
from imageio import imwrite


def extractNote(element):
    return int(element.pitch.ps)


def extractDuration(element):
    return element.duration.quarterLength


def get_notes(notes_to_parse):

    """ Get all the notes and chords from the midi files in the ./midi_songs directory """
    durations = []
    notes = []
    start = []

    for element in notes_to_parse:
        if isinstance(element, note.Note):
            if element.isRest:
                continue

            start.append(element.offset)
            notes.append(extractNote(element))
            durations.append(extractDuration(element))

        elif isinstance(element, chord.Chord):
            if element.isRest:
                continue
            for chord_note in element.notes:
                start.append(element.offset)
                durations.append(extractDuration(element))
                notes.append(extractNote(chord_note))

    return {"start": start, "pitch": notes, "dur": durations}


def midi_to_image(midi_path, image_path):
    mid = converter.parse(midi_path)
    instruments = instrument.partitionByInstrument(mid)
    data = {}

    try:
        i = 0
        for instrument_i in instruments.parts:
            notes_to_parse = instrument_i.recurse()

            if instrument_i.partName is None:
                data["instrument_{}".format(i)] = get_notes(notes_to_parse)
                i += 1
            else:
                data[instrument_i.partName] = get_notes(notes_to_parse)

    except:
        notes_to_parse = mid.flat.notes
        data["instrument_0".format(i)] = get_notes(notes_to_parse)

    resolution = 1 / 16

    for instrument_name, values in data.items():
        # https://en.wikipedia.org/wiki/Scientific_pitch_notation#Similar_systems
        upperBoundNote = 128
        lowerBoundNote = 0
        maxSongLength = 1024

        index = 0
        prev_index = 0
        repetitions = 0
        non_empty = True

        while non_empty:

            if prev_index >= len(values["pitch"]):
                break

            matrix = np.zeros((upperBoundNote - lowerBoundNote, maxSongLength))

            pitchs = values["pitch"]
            durs = values["dur"]
            starts = values["start"]
            non_empty = False

            for i in range(prev_index, len(pitchs)):
                pitch = pitchs[i]

                dur = int(durs[i] / resolution)
                start = int(starts[i] / resolution)

                if dur + start - index * maxSongLength < maxSongLength:

                    for j in range(start, start + dur):

                        if j - index * maxSongLength >= 0:
                            matrix[
                                pitch - lowerBoundNote, j - index * maxSongLength
                            ] = 255
                            non_empty = True

                else:
                    prev_index = i
                    break

            matrix = np.argmax(matrix, axis=0)
            matrix = matrix.astype(float)
            matrix = (matrix / 128.0) * 255.0
            matrix = np.reshape(matrix, (32, 32))
            matrix = matrix.astype(np.uint8)

            doinu_path = midi_path.split("/")[-1].replace(
                ".mid", f"_{instrument_name}_{index}.png"
            )
            image_filepath = os.path.join(image_path, doinu_path)

            if non_empty:
                imwrite(image_filepath, matrix)

            index += 1
            repetitions += 1
