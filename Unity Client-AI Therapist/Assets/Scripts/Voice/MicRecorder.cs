using UnityEngine;
using System;

public class MicRecorder : MonoBehaviour
{
    public Action<AudioClip> OnRecordingComplete;

    private AudioClip clip;
    private bool recording;

    public void StartRecording()
    {
        if (recording) return;
        recording = true;
        clip = Microphone.Start(null, false, 10, 44100);
    }

    public void StopRecording()
    {
        if (!recording) return;
        recording = false;
        Microphone.End(null);
        OnRecordingComplete?.Invoke(clip);
    }
}
