using UnityEngine;

public class IdleLifeController : MonoBehaviour
{
    [Header("Breathing")]
    public Transform chest;              // optional (can be null)
    public float breatheSpeed = 1.2f;
    public float breatheAmount = 0.015f;

    [Header("Head Motion")]
    public Transform head;
    public float headSwaySpeed = 0.6f;
    public float headSwayAmount = 1.5f;

    [Header("Blinking")]
    public SkinnedMeshRenderer faceMesh;
    public int eyeCloseBlendShape = 0;
    public float blinkMinDelay = 2.5f;
    public float blinkMaxDelay = 5f;

    private float blinkTimer;
    private bool blinking;
    private float blinkWeight;

    private Vector3 chestStartPos;
    private Quaternion headStartRot;

    void Start()
    {
        if (chest != null)
            chestStartPos = chest.localPosition;

        if (head != null)
            headStartRot = head.localRotation;

        ResetBlinkTimer();
    }

    void Update()
    {
        DoBreathing();
        DoHeadSway();
        DoBlink();
    }

    void DoBreathing()
    {
        if (chest == null) return;

        float offset = Mathf.Sin(Time.time * breatheSpeed) * breatheAmount;
        chest.localPosition = chestStartPos + Vector3.up * offset;
    }

    void DoHeadSway()
    {
        if (head == null) return;

        float sway = Mathf.Sin(Time.time * headSwaySpeed) * headSwayAmount;
        Quaternion rot = Quaternion.Euler(0, sway, 0);
        head.localRotation = headStartRot * rot;
    }

    void DoBlink()
    {
        if (faceMesh == null) return;

        blinkTimer -= Time.deltaTime;

        if (!blinking && blinkTimer <= 0)
        {
            blinking = true;
            blinkWeight = 0;
        }

        if (blinking)
        {
            blinkWeight += Time.deltaTime * 600f;
            float weight = Mathf.PingPong(blinkWeight, 100f);
            faceMesh.SetBlendShapeWeight(eyeCloseBlendShape, weight);

            if (blinkWeight >= 200f)
            {
                faceMesh.SetBlendShapeWeight(eyeCloseBlendShape, 0);
                blinking = false;
                ResetBlinkTimer();
            }
        }
    }

    void ResetBlinkTimer()
    {
        blinkTimer = Random.Range(blinkMinDelay, blinkMaxDelay);
    }
}
