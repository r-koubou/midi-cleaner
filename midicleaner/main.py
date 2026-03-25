import sys
import pretty_midi

def main(argv):

    input_file  = argv[0]
    output_file = argv[1]
    midi        =  pretty_midi.PrettyMIDI(input_file, resolution=480)
    midi_tracks = midi.instruments

    for t in midi_tracks:
        t.name    = ""
        t.control_changes = []

    midi.write(output_file)

def usage():
    print("Usage: midicleaner.py <input midi_file> <output midi_file>")

if __name__ == '__main__':
    if(len(sys.argv) < 3):
        usage()
        sys.exit(1)

    main(sys.argv[1:])
