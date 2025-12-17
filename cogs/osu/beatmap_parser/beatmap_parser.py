import os
import re


class BeatmapParser:
    def __init__(self, filepath=None, content=None):
        self.filepath = filepath
        self.content = content
        self.metadata = {}
        self.difficulty = {}
        self.timing_points = []
        self.hit_objects = []
        
        if filepath and os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                self.content = f.read()
        
        if self.content:
            self.parse()
    
    def parse(self):
        if not self.content:
            return
        
        lines = self.content.split('\n')
        current_section = None
        
        for line in lines:
            line = line.strip()
            
            if line.startswith('[') and line.endswith(']'):
                current_section = line[1:-1]
                continue
            
            if not line or line.startswith('//'):
                continue
            
            if current_section == 'Metadata':
                self._parse_metadata(line)
            elif current_section == 'Difficulty':
                self._parse_difficulty(line)
            elif current_section == 'TimingPoints':
                self._parse_timing_point(line)
            elif current_section == 'HitObjects':
                self._parse_hit_object(line)
    
    def _parse_metadata(self, line):
        if ':' in line:
            key, value = line.split(':', 1)
            self.metadata[key.strip()] = value.strip()
    
    def _parse_difficulty(self, line):
        if ':' in line:
            key, value = line.split(':', 1)
            try:
                self.difficulty[key.strip()] = float(value.strip())
            except ValueError:
                self.difficulty[key.strip()] = value.strip()
    
    def _parse_timing_point(self, line):
        parts = line.split(',')
        if len(parts) >= 2:
            self.timing_points.append({
                'time': float(parts[0]),
                'beat_length': float(parts[1])
            })
    
    def _parse_hit_object(self, line):
        parts = line.split(',')
        if len(parts) >= 3:
            self.hit_objects.append({
                'x': int(parts[0]),
                'y': int(parts[1]),
                'time': int(parts[2])
            })
    
    def get_title(self):
        return self.metadata.get('Title', 'Unknown')
    
    def get_artist(self):
        return self.metadata.get('Artist', 'Unknown')
    
    def get_creator(self):
        return self.metadata.get('Creator', 'Unknown')
    
    def get_version(self):
        return self.metadata.get('Version', 'Unknown')
    
    def get_cs(self):
        return self.difficulty.get('CircleSize', 5.0)
    
    def get_ar(self):
        return self.difficulty.get('ApproachRate', 5.0)
    
    def get_od(self):
        return self.difficulty.get('OverallDifficulty', 5.0)
    
    def get_hp(self):
        return self.difficulty.get('HPDrainRate', 5.0)


beatmap_parser = BeatmapParser
