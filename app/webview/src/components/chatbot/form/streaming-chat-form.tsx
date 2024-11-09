import { useRef, FormEvent } from 'react';
import { Textarea } from '@/components/ui/textarea';
import { Button } from '@/components/ui/button';
import { SendHorizonal } from 'lucide-react';

type Props = {
    prompt: string
    onChangePrompt: (value: string) => void
    action: (e: FormEvent<HTMLFormElement>) => void
}

export const StreamingChatForm = ({
    prompt,
    onChangePrompt,
    action,
}: Props) => {
    const hiddenInput = useRef<HTMLDivElement>(null)

    const handleTextareaChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
        onChangePrompt(e.target.value);
        if (hiddenInput.current) {
            hiddenInput.current.textContent = e.target.value + '\u200b';
        }
    };

    return (
        <form onSubmit={action} className={'max-h-[25dvh] max-h-52 overflow-auto w-full flex justify-end items-center rounded-lg py-4 px-2 bg-gray-300'}>
            <div className={'relative w-full flex'}>
                <div
                    className="invisible min-h-10 overflow-hidden whitespace-pre-wrap break-words"
                    aria-hidden={true}
                    ref={hiddenInput}
                >
                </div>
                <Textarea
                    className="absolute top-0 left-0 w-full min-h-fit h-full resize-none outline-none border-none shadow-none focus-visible:ring-0"
                    onChange={handleTextareaChange}
                    value={prompt}
                    placeholder={'AIに相談'}
                />
            </div>
            <div className={'flex gap-1'}>
                <Button type="submit" size={'icon'} variant={'ghost'}><SendHorizonal/></Button>
            </div>
        </form>
    );
}