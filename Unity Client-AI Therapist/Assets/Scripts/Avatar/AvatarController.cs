using UnityEngine;

public class AvatarController : MonoBehaviour
{
    [SerializeField] private Animator animator;
    [SerializeField] private AudioPlayer audioPlayer;
    [SerializeField] private SkinnedMeshRenderer faceMesh;
    [SerializeField] private int mouthBlendShapeIndex = 0;

    void Update()
    {
        if (audioPlayer == null) return;

        float amp = audioPlayer.GetAmplitude();
        float weight = Mathf.Clamp(amp * 200f, 0f, 100f);

        faceMesh.SetBlendShapeWeight(mouthBlendShapeIndex, weight);

        animator.SetBool("isTalking", amp > 0.01f);
    }
}
