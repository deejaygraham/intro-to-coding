# Sonic Pi

Sam Aaron came to Super Mondays to perform live coding a while ago.

play 60 
sleep 0.25 (seconds)

or use Play :C4

# comments

# put hash before lines


# Lists of notes

play_pattern [40, 45, 44, 43 ] (using current tempo)

play_pattern_timed [40, 45, 44, 43], [0.5, 1, 10] // times loop if not enough provided


# Chords

play_chord [40, 10, 99]

## Incidentals 

play :Cs3

or 

play :Db4

# Repeats

Repeat forever

repeat do

    play 60
    sleep 0.25

end

3.times do

end

# Tempo

with_tempo 150

current_tempo 

with_tempo current_tempo * 2

# Threads

# take this code and run in concurrently with whatever follows

in_thread do

    2.times do
    # indentation is your friend..
     play 60
     sleep 0.5
    end
end

# Stop

stops all sounds

# Variables

half_note = 1
minim = half_note / 2

# Functions 

# sad trombone

# bad guy riff

define :trombone do
    play 
end

transcribing from standard music notation...
